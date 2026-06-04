# PourVous 在庫管理 — デスクトップショートカット（かわいいアイコン付き）
$ErrorActionPreference = 'Stop'
$AppUrl = 'https://pourvous-inventory.web.app/'
$AppName = [char]0x30D7 + [char]0x30A5 + [char]0x30EB + [char]0x30FB + [char]0x30F4 + [char]0x30FC + [char]0x5728 + [char]0x5EAB + [char]0x7BA1 + [char]0x7406
$IconPath = Join-Path $PSScriptRoot 'icons\favicon.ico'
$Desktop = [Environment]::GetFolderPath('Desktop')
$ShortcutPath = Join-Path $Desktop ($AppName + '.lnk')

$edgePaths = @(
    "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe",
    "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe",
    "$env:LocalAppData\Google\Chrome\Application\chrome.exe",
    "$env:ProgramFiles\Google\Chrome\Application\chrome.exe"
)
$browser = $edgePaths | Where-Object { Test-Path $_ } | Select-Object -First 1

if (-not $browser) {
    $urlPath = Join-Path $Desktop ($AppName + '.url')
    $content = "[InternetShortcut]`r`nURL=$AppUrl`r`nIconFile=$IconPath`r`nIconIndex=0`r`n"
    Set-Content -Path $urlPath -Value $content -Encoding ASCII
    Write-Host "Created: $urlPath"
    exit 0
}

$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($ShortcutPath)
$Shortcut.TargetPath = $browser
$Shortcut.Arguments = "--app=$AppUrl"
$Shortcut.IconLocation = "$IconPath,0"
$Shortcut.Description = $AppName
$Shortcut.Save()

Write-Host "Created: $ShortcutPath"
Write-Host "URL: $AppUrl"
Write-Host "Icon: $IconPath"
