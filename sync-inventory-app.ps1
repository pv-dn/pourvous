# 開発用: pourvous\在庫管理.html の変更を Downloads の PWA 用ファイルへ反映
# ユーザーの元アプリを上書きしないよう、手動で restore-user-app.py を先に確認すること
$ErrorActionPreference = 'Stop'
Write-Host 'Use restore-user-app.py to restore the user PWA copy from backup.'
Write-Host 'Do not auto-sync pourvous deploy HTML to Downloads without explicit request.'
