[English](README.md) | [简体中文](README.zh-CN.md)

# SCI Studio · 战略传播智能工作台

SCI Studio 帮助你处理公关、传播与品牌决策：明确目标，比较选择与风险，形成实际行动和沟通材料。它既可作为本地桌面应用连接你选择的模型 API，也可作为 Agent Skill 使用兼容宿主的模型与工具。

**公开 Alpha 预发布，可供个人及企业内部评估，不是稳定产品。** 尚未证明整体优于普通 AI。对外使用文字前，请核对事实、进度和承诺。

仓库保持为 **`ninghan-notbot/ai-pr-advisor`**。Skill 标识、应用数据标识及冻结附件名称继续保留 `ai-pr-advisor`，以兼容已有安装。

## 下载冻结候选

| 下载入口 | 版本与实际范围 |
|---|---|
| [Mac · Apple 芯片](https://github.com/ninghan-notbot/ai-pr-advisor/releases/download/desktop-v0.7.0-alpha.13/ai-pr-advisor-desktop-0.7.0-alpha.13-mac-arm64.zip) | 桌面 **0.7.0-alpha.13**；已在 Apple 芯片 Mac 使用下述 DeepSeek 配置实测。没有 Intel Mac 构建。 |
| [Windows · x64 便携 EXE](https://github.com/ninghan-notbot/ai-pr-advisor/releases/download/desktop-v0.7.0-alpha.13/ai-pr-advisor-desktop-0.7.0-alpha.13-win-x64.exe) | 桌面 **0.7.0-alpha.13**；**本版未在 Windows 实机运行**。包内程序相同不等于原生兼容性通过。 |
| [完整 Agent Skill ZIP](https://github.com/ninghan-notbot/ai-pr-advisor/releases/download/desktop-v0.7.0-alpha.13/ai-pr-advisor-skill-0.7.0-content.7-generic.zip) | 专业内容 **0.7.0-content.7**，与 Alpha13 内置内容同源；**尚未在 WorkBuddy 或其他宿主安装验证**。 |

[发布说明／安装详情](https://github.com/ninghan-notbot/ai-pr-advisor/releases/tag/desktop-v0.7.0-alpha.13) · [SHA-256 校验清单](https://github.com/ninghan-notbot/ai-pr-advisor/releases/download/desktop-v0.7.0-alpha.13/SHA256SUMS.txt)

**请使用上述专用附件。** GitHub 自动生成的 “Source code” 压缩包不是桌面应用，包含的是仓库旧版 Skill。克隆 `main`、直接导入仓库地址或使用旧安装清单，**都不能安装 content.7**。

## 开始使用

**桌面版：** 下载对应附件，解压 Mac ZIP 或打开 Windows 便携 EXE，然后进入“**模型与设置**”。选择服务商，填写自己的 API Key 和模型，检查用量上限后确认请求授权。用中文或英文自然说明目标、市场、事实和可用资源。支持 TXT、Markdown、CSV 材料；不支持读取图片、PDF 和 Word。

应用提供 13 家服务商预设及自定义兼容接口。**本候选仅实测了 Apple 芯片 Mac 上的 DeepSeek 官方 `deepseek-v4-pro`，联网搜索关闭。** 其他预设不等于真实连接通过；Alpha13 未重新验证原生联网搜索。模型费用由服务商收取；应用不会自动充值，也不会在失败后自动重试。估算用量上限不是服务商账单保证。

未签名程序可能触发系统提示，处理方法见发布说明；无需全局关闭系统安全防护。

**Skill：** 下载上方完整的 **content.7 ZIP**，使用宿主正式支持的自定义 Skill 导入入口，保留 `SKILL.md` 和全部参考文件。在新任务中按宿主提供的方式启用或选择技能。WorkBuddy 对 content.7 的导入和调用尚未实测；旧版 0.6.4-draft.2 的手动导入记录不能计作新版通过。自然语言安装是体验目标，尚非已验证能力。账户资格、工具、模型和费用由宿主决定。

## 版本、数据与限制

- 桌面：**0.7.0-alpha.13**。内置专业内容及下载的 Skill：**0.7.0-content.7**。
- **Code／main 仍为 Skill 0.6.4-draft.2。** 其文件及安装记录作为历史材料保留，不是新版 Skill 安装路径。
- 桌面源码不公开。此仓库保留原有公开 Skill、公开说明和发行下载入口。
- 桌面项目与材料在本机以**未加密 JSON** 保存。相关项目记录、近期对话和专业指南会发送给你选择的模型服务商。API Key 使用受保护的本地存储或仅会话保存。保留及训练政策由服务商条款决定；Skill 的数据处理取决于宿主。
- 小样本测试不等于普遍可靠。草稿仍可能增加没有依据的服务、日期、进度或承诺。请核对对外文字，并填好或删除占位符。模型生成的“本稿写入／不写入”依据行不是独立核验；复制整条回答可能同时包含分析和草稿。

## 许可与署名

- **Skill 和原创专业总结：** [MIT 许可证](LICENSE)，content.7 ZIP 内也包含完整许可证。
- **桌面二进制：** [桌面 Alpha 评估许可](https://github.com/ninghan-notbot/ai-pr-advisor/releases/download/desktop-v0.7.0-alpha.13/DESKTOP_LICENSE.txt)，允许个人或内部评估使用官方未修改安装包，不代表桌面源码公开或开源。
- 第三方出版物保留其权利，来源链接见包内说明。[项目标识说明](TRADEMARKS.md)保留正常署名，不暗示官方背书。不分发私有研究库或咨询原文。
