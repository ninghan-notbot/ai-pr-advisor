import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from install import install
from package import payload, SECRET
spec = importlib.util.spec_from_file_location('session', ROOT / 'scripts/session.py')
session = importlib.util.module_from_spec(spec)
spec.loader.exec_module(session)


class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.empty = dict(schema_version=1, language='zh', events=[])

    def test_internal_assessment_remains_internal_until_explicit_evidenced_revision(self):
        doc, first = session.add(self.empty, 'internal', 'opening-hours', 'Opening at 14:00 proposed', 'Manager')
        with self.assertRaises(ValueError):
            session.add(doc, 'verified', 'opening-hours', 'Confirmed', supersedes=first)
        with self.assertRaises(ValueError):
            session.add(doc, 'verified', 'opening-hours', 'Passed', 'Roster', 'Tested version')
        revised, _ = session.add(doc, 'verified', 'opening-hours', 'Passed', 'Report A', 'Version B', first)
        self.assertEqual(['internal', 'verified'], [x['kind'] for x in revised['events']])
        self.assertEqual('internal', doc['events'][0]['kind'])

    def test_new_information_can_retract_and_preserves_history(self):
        doc, first = session.add(self.empty, 'assumption', 'opening-hours', 'Open at 14:00 if staff available')
        revised, second = session.add(doc, 'unknown', 'opening-hours', 'Staff unavailable; reassess', 'User', '', first)
        with self.assertRaises(ValueError):
            session.add(revised, 'decision', 'opening-hours', 'Announce revised hours', supersedes=first)
        self.assertEqual(2, len(revised['events']))
        self.assertNotEqual(first, second)

    def test_rejects_cross_claim_revision(self):
        doc, first = session.add(self.empty, 'internal', 'claim-a', 'A')
        with self.assertRaises(ValueError):
            session.add(doc, 'internal', 'claim-b', 'B', supersedes=first)

    def test_round_trip_chinese_and_private_permissions(self):
        with tempfile.TemporaryDirectory() as d:
            target = Path(d) / 'record.json'
            doc, _ = session.add(self.empty, 'unknown', 'report', '正式报告尚未取得')
            session.write(target, doc)
            self.assertEqual(doc, session.load(target))
            self.assertEqual(0o600, target.stat().st_mode & 0o777)


class InstallTests(unittest.TestCase):
    def test_actual_zip_layouts_include_license_and_same_payload(self):
        with tempfile.TemporaryDirectory() as d:
            archives={}
            for layout in ['directory','flat']:
                target=Path(d)/(layout+'.zip')
                subprocess.run([sys.executable,str(ROOT/'tools/package.py'),'--layout',layout,'--output',str(target)],check=True,capture_output=True)
                with zipfile.ZipFile(target) as archive:
                    prefix='ai-pr-advisor/' if layout=='directory' else ''
                    self.assertIn(prefix+'SKILL.md',archive.namelist())
                    self.assertIn(prefix+'LICENSE',archive.namelist())
                    self.assertIn(prefix+'NOTICE.md',archive.namelist())
                    archives[layout]={name.removeprefix(prefix):archive.read(name) for name in archive.namelist()}
            self.assertEqual(archives['directory'],archives['flat'])
            self.assertEqual(payload(),archives['flat'])
    def test_token_boundaries_do_not_reject_a_risk_framework_url(self):
        self.assertIsNone(SECRET.search('https://www.nist.gov/itl/ai-risk-management-framework'))
        self.assertIsNotNone(SECRET.search('token = '+ 'sk-' + 'x'*32))
    def test_install_is_idempotent_and_refuses_unreviewed_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            dest, status = install(d, 'codex', {'SKILL.md': b'example'})
            self.assertEqual('installed', status)
            self.assertEqual('already_identical', install(d, 'codex', {'SKILL.md': b'example'})[1])
            with self.assertRaises(ValueError):
                install(d, 'codex', {'SKILL.md': b'changed'})
            self.assertEqual(b'example', (dest / 'SKILL.md').read_bytes())

    def test_destination_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / 'elsewhere').mkdir()
            (p / '.agents').symlink_to(p / 'elsewhere', target_is_directory=True)
            with self.assertRaises(ValueError):
                install(p, 'codex', {'SKILL.md': b'example'})

    def test_package_rejects_escape_and_private_paths(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / 'package-files.json').write_text(json.dumps(['../outside']))
            with self.assertRaises(ValueError):
                payload(p)
            (p / 'package-files.json').write_text(json.dumps(['SKILL.md']))
            (p / 'SKILL.md').write_text('/Volumes/private/research')
            with self.assertRaises(ValueError):
                payload(p)

    def test_package_excludes_unlisted_private_file(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / 'package-files.json').write_text(json.dumps(['SKILL.md']))
            (p / 'SKILL.md').write_text('skill')
            (p / 'private.txt').write_text('DO NOT DISTRIBUTE')
            self.assertEqual({'SKILL.md': b'skill'}, payload(p))


if __name__ == '__main__':
    unittest.main()
