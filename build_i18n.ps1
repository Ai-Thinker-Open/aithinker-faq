<#
.SYNOPSIS
    一键完成翻译文件更新与中英文双语言构建（Windows PowerShell）。

.DESCRIPTION
    默认执行两件事：
      1) 从源文档提取可翻译文本，增量更新英文 .po 文件（source\locale\en）；
      2) 本地预览用：构建中文站点到 build\html，英文站点到 build\html\en。
    线上采用 RTD 官方翻译方案（同一仓库 + 两个已关联的 RTD 项目，各构建一种语言），
    语言切换器由 RTD 平台自动提供，本脚本仅用于本地双语预览与翻译更新。

.PARAMETER UpdateOnly
    仅更新 .po 翻译文件，不进行 HTML 构建。

.PARAMETER BuildOnly
    仅构建双语言 HTML，不更新 .po 翻译文件。

.EXAMPLE
    ./build_i18n.ps1
    更新翻译并构建中英文站点。

.EXAMPLE
    ./build_i18n.ps1 -UpdateOnly
    仅在文档内容变更后刷新英文 .po 文件。
#>
param(
    [switch]$UpdateOnly,
    [switch]$BuildOnly
)

$ErrorActionPreference = 'Stop'

# 切换到脚本所在目录（项目根目录）
Set-Location -Path $PSScriptRoot

$SourceDir = 'source'
$BuildDir = 'build'
$GettextDir = Join-Path $BuildDir 'gettext'
$HtmlDir = Join-Path $BuildDir 'html'
$HtmlEnDir = Join-Path $HtmlDir 'en'

function Update-Translations {
    Write-Host '[1/2] 提取可翻译文本并更新英文 .po 文件...' -ForegroundColor Cyan
    sphinx-build -b gettext $SourceDir $GettextDir
    if ($LASTEXITCODE -ne 0) { throw 'gettext 提取失败' }

    sphinx-intl update -p $GettextDir -l en -d (Join-Path $SourceDir 'locale')
    if ($LASTEXITCODE -ne 0) { throw 'sphinx-intl 更新失败' }

    # 清理临时的 pot 目录
    if (Test-Path $GettextDir) {
        Remove-Item -Recurse -Force $GettextDir
    }
    Write-Host '翻译文件已更新：source\locale\en\LC_MESSAGES\*.po' -ForegroundColor Green
}

function Build-Docs {
    Write-Host '[2/2] 构建中文站点 -> build\html ...' -ForegroundColor Cyan
    sphinx-build -b html $SourceDir $HtmlDir
    if ($LASTEXITCODE -ne 0) { throw '中文站点构建失败' }

    Write-Host '构建英文站点 -> build\html\en ...' -ForegroundColor Cyan
    sphinx-build -b html -D language=en $SourceDir $HtmlEnDir
    if ($LASTEXITCODE -ne 0) { throw '英文站点构建失败' }

    Write-Host '构建完成：中文 build\html，英文 build\html\en' -ForegroundColor Green
}

if ($BuildOnly) {
    Build-Docs
}
elseif ($UpdateOnly) {
    Update-Translations
}
else {
    Update-Translations
    Build-Docs
}
