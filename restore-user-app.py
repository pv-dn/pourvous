"""Restore user's original inventory HTML (no pourvous deploy version)."""
import shutil
from pathlib import Path

BACKUP = Path(
    r"C:\Users\e--yo\AppData\Local\Microsoft\Olk\Attachments"
    r"\ooa-088f5701-62da-4424-89a0-e3dc87bdb39b"
    r"\1ee1d1b5f78831d0256830c244f8971725acddf0c7c9b4c139df151ab85caefb"
    r"\プゥル・ヴー在庫管理.html"
)
DOWNLOADS = Path.home() / "Downloads"
TARGETS = [
    DOWNLOADS / "プゥル・ヴー在庫管理_19.html",
    DOWNLOADS / "プゥル・ヴー在庫管理.html",
]

if not BACKUP.exists():
    raise SystemExit(f"Backup not found: {BACKUP}")

for target in TARGETS:
    shutil.copy2(BACKUP, target)
    print(f"Restored: {target}")
