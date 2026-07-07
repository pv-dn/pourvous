"""512px PNG から Windows デスクトップ用の複数解像度 ICO を生成する。"""
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
SRC = HERE / "icon-512.png"
OUT = HERE / "desktop.ico"

SIZES = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]


def main() -> None:
    img = Image.open(SRC)
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    img.save(OUT, format="ICO", sizes=SIZES)
    print(f"Wrote {OUT} ({', '.join(f'{w}x{h}' for w, h in SIZES)})")


if __name__ == "__main__":
    main()
