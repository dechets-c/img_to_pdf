import argparse
from pathlib import Path
import logging
import glob

from PIL import Image


def convert_to_pdf(path: Path):
    export_path = path.parent / (path.stem + ".pdf")
    with Image.open(path) as img:
        img = img.convert("RGB")
        print(export_path)
        img.save(export_path)


def main():
    parser = argparse.ArgumentParser(
        prog="img_to_pdf", description="Small cli that convert images to pdf"
    )
    parser.add_argument("files", nargs="+")
    parser.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()

    files = []
    for pattern in args.files:
        files.extend([Path(f) for f in glob.glob(pattern)])
    for file in files:
        convert_to_pdf(file)


if __name__ == "__main__":
    main()
