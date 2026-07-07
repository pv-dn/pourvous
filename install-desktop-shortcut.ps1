# PourVous 在庫管理 — デスクトップショートカット（Chrome インストール版 PWA）
# https://pourvous-inventory.web.app/ および pourvous/index.html への差し替えはしない
$ErrorActionPreference = 'Stop'
$AppName = [char]0x30D7 + [char]0x30A5 + [char]0x30EB + [char]0x30FB + [char]0x30F4 + [char]0x30FC + [char]0x5728 + [char]0x5EAB + [char]0x7BA1 + [char]0x7406
$IconPath = Join-Path $PSScriptRoot 'icons\desktop.ico'
if (-not (Test-Path $IconPath)) {
    python (Join-Path $PSScriptRoot 'icons\make-desktop-ico.py') | Out-Null
}

$DesktopDir = Join-Path $env:USERPROFILE 'OneDrive\Desktop'
$shortcutFile = Get-ChildItem -LiteralPath $DesktopDir -Filter 'PourVous*.lnk' -ErrorAction Stop | Select-Object -First 1

$chromeProxy = "$env:ProgramFiles\Google\Chrome\Application\chrome_proxy.exe"
if (-not (Test-Path $chromeProxy)) { throw 'chrome_proxy.exe が見つかりません' }

$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($shortcutFile.FullName)
$Shortcut.TargetPath = $chromeProxy
$Shortcut.Arguments = '--profile-directory=Default --app-id=fjdfpjippadiknpllhijkfnbcajpnbbo'
$Shortcut.IconLocation = "$IconPath,0"
$Shortcut.Description = $AppName
$Shortcut.Save()

Write-Host "Updated (Chrome PWA): $($shortcutFile.FullName)"
