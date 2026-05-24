import importlib
import subprocess
import sys
from pathlib import Path


REQUIRED = {
    "fitz": ("pymupdf", lambda module: hasattr(module, "open") and hasattr(module, "Rect")),
    "PIL.Image": ("pillow", lambda module: hasattr(module, "open")),
    "pdfplumber": ("pdfplumber", lambda module: hasattr(module, "open")),
    "pypdf": ("pypdf", lambda module: hasattr(module, "PdfReader")),
}


def missing_packages() -> list[str]:
    missing = []
    for module_name, (package, validator) in REQUIRED.items():
        try:
            module = importlib.import_module(module_name)
        except Exception:
            missing.append(package)
            continue
        if not validator(module):
            missing.append(package)
    return missing


def main() -> int:
    missing = missing_packages()
    if not missing:
        print("All remote-sensing-paper-brief Python dependencies are installed.")
        return 0

    req = Path(__file__).with_name("requirements.txt")
    print("Missing packages:", ", ".join(missing))
    print(f"Installing from {req}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(req)])
    print("Dependencies installed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
