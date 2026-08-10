[![English](https://img.shields.io/badge/English-文档-green)](VALIDATION.md)

# 验证说明

## 复现校验

```powershell
python -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install -r docs/requirements.txt
python tools/validate_repository.py
```

校验工具会检查：

1. 每个 `.rst` 文档都有对应路径的英文 `.po` 和 `.mo`，且不存在孤立目录。
2. 每条有效 gettext 消息都已翻译，且没有有效消息带 `fuzzy` 标记。
3. 英文目录可成功编译。
4. 简体中文和英文 HTML 均能从全新 doctree 构建，且 Sphinx 警告按错误处理。

最近一次提交的结果保存在 `docs/validation-logs/Sphinx-validation.log`，机器可读证据保存在 `docs/technical-evidence.json`。

## 范围与限制

本仓库是文档项目，因此不存在固件编译、设备烧录、硬件在环测试或运行时单元测试。线上配置只请求 HTML，可选 PDF、EPUB 和 HTML ZIP 构建器不在声明的发布范围内。校验不测试外部站点可用性，因此通过代表 reST、翻译目录和构建完整，不代表第三方链接永久可用或内容正确。
