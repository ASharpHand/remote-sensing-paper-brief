import argparse
import sys
from pathlib import Path

import fitz
from PIL import Image


def render_region(pdf_path: Path, page_number: int, output_path: Path, dpi: int, crop: str | None) -> None:
    if not pdf_path.is_file():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")
    if page_number < 1:
        raise ValueError("--page must be a 1-based page number greater than 0")
    if dpi < 72:
        raise ValueError("--dpi must be at least 72")

    doc = fitz.open(pdf_path)
    try:
        if page_number > doc.page_count:
            raise ValueError(f"--page {page_number} is outside the PDF page range 1-{doc.page_count}")

        page = doc[page_number - 1]
        clip = None
        if crop:
            try:
                parts = [float(x.strip()) for x in crop.split(",")]
            except ValueError as exc:
                raise ValueError("--crop must contain four numbers: x0,y0,x1,y1") from exc
            if len(parts) != 4:
                raise ValueError("--crop must be x0,y0,x1,y1 in PDF points")
            clip = fitz.Rect(*parts)
            if clip.is_empty or clip.x1 <= clip.x0 or clip.y1 <= clip.y0:
                raise ValueError("--crop must have x1 > x0 and y1 > y0")
            if not clip.intersects(page.rect):
                raise ValueError("--crop does not overlap the selected PDF page")

        matrix = fitz.Matrix(dpi / 72, dpi / 72)
        pix = page.get_pixmap(matrix=matrix, colorspace=fitz.csRGB, alpha=False, clip=clip)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        pix.save(output_path)

        with Image.open(output_path) as img:
            if img.mode != "RGB":
                img = img.convert("RGB")
            img.save(output_path)
    finally:
        doc.close()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render a PDF page or page region as a white-background RGB PNG for method figures."
    )
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--page", type=int, required=True, help="1-based PDF page number")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--dpi", type=int, default=240)
    parser.add_argument(
        "--crop",
        help="Optional crop rectangle in PDF points: x0,y0,x1,y1. Omit to render the full page.",
    )
    args = parser.parse_args()
    try:
        render_region(args.pdf, args.page, args.out, args.dpi, args.crop)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
