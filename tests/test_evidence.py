import importlib.util
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('checker',ROOT/'tools/check_evaluation.py')
checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
class EvidenceTests(unittest.TestCase):
    def test_self_claim_is_not_a_tool_read(self):
        events=[dict(type='item.completed',item=dict(type='agent_message',text='I read the skill. Complete instructions.'))]
        self.assertEqual([],checker.observed_reads(events,{'SKILL.md':'Complete instructions.'}))
    def test_failed_command_is_not_successful_read(self):
        events=[dict(type='item.completed',item=dict(type='command_execution',exit_code=1,aggregated_output='Complete instructions.'))]
        self.assertEqual([],checker.observed_reads(events,{'SKILL.md':'Complete instructions.'}))
    def test_partial_file_is_not_full_read(self):
        events=[dict(type='item.completed',item=dict(type='command_execution',exit_code=0,aggregated_output='First section.'))]
        self.assertEqual([],checker.observed_reads(events,{'SKILL.md':'First section. Second section.'}))
    def test_successful_complete_file_read(self):
        events=[dict(type='item.completed',item=dict(type='command_execution',exit_code=0,aggregated_output='Complete instructions.'))]
        self.assertEqual(['SKILL.md'],checker.observed_reads(events,{'SKILL.md':'Complete instructions.'}))
if __name__=='__main__':unittest.main()
