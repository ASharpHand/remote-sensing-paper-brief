from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


SKILL_NAME = "remote-sensing-paper-brief"
MIN_PYTHON = (3, 10)
VENV_DIR = Path.home() / ".codex" / "skill-envs" / SKILL_NAME / ".venv"
REQUIREMENTS = Path(__file__).with_name("requirements.txt")

REQUIRED = {
    "fitz": ("pymupdf", ("open", "Rect")),
    "PIL.Image": ("pillow", ("open",)),
    "pdfplumber": ("pdfplumber", ("open",)),
    "pypdf": ("pypdf", ("PdfReader",)),
}


def run(cmd: list[str]) -> None:
    print("+", " ".join(f'"{part}"' if " " in part else part for part in cmd))
    subprocess.check_call(cmd)


def venv_python_candidates() -> list[Path]:
    if os.name == "nt":
        return [VENV_DIR / "Scripts" / "python.exe"]
    return [VENV_DIR / "bin" / "python"]


def venv_python() -> Path | None:
    for python in venv_python_candidates():
        if python.exists():
            return python
    return None


def python_version(command: list[str]) -> tuple[int, int] | None:
    code = "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
    try:
        output = subprocess.check_output(command + ["-c", code], text=True, stderr=subprocess.DEVNULL)
    except Exception:
        return None

    try:
        major, minor = output.strip().split(".", 1)
        return int(major), int(minor)
    except Exception:
        return None


def is_supported_python(command: list[str]) -> bool:
    version = python_version(command)
    return bool(version and version >= MIN_PYTHON)


def python_executable(path: str) -> list[str]:
    expanded = Path(path).expanduser()
    return [str(expanded)]


def find_python310(explicit_python: str | None = None) -> list[str] | None:
    if explicit_python:
        command = python_executable(explicit_python)
        if is_supported_python(command):
            return command
        raise RuntimeError(f"{explicit_python} is not Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+.")

    candidates = [
        [sys.executable],
        ["py", "-3.12"],
        ["py", "-3.11"],
        ["py", "-3.10"],
        ["python3.12"],
        ["python3.11"],
        ["python3.10"],
        ["python3"],
        ["python"],
    ]
    for candidate in candidates:
        if is_supported_python(candidate):
            return candidate
    return None


def ensure_supported_python(python: Path) -> None:
    if not is_supported_python([str(python)]):
        raise RuntimeError(
            f"{python} is not Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+. "
            "Remove or recreate the venv, then rerun this setup script."
        )


def create_venv(explicit_python: str | None = None) -> Path:
    creator = find_python310(explicit_python)
    if not creator:
        raise RuntimeError(
            "No Python 3.10+ interpreter was found. Install Python 3.10 or later from python.org, "
            "or rerun this setup script with --python <path-to-python-3.10+>."
        )

    VENV_DIR.parent.mkdir(parents=True, exist_ok=True)
    run(creator + ["-m", "venv", str(VENV_DIR)])

    python = venv_python()
    if not python:
        raise RuntimeError(f"Virtual environment was created, but no Python executable was found under {VENV_DIR}.")
    ensure_supported_python(python)
    return python


def ensure_venv(explicit_python: str | None = None) -> Path:
    existing = venv_python()
    if existing:
        ensure_supported_python(existing)
        return existing

    if VENV_DIR.exists():
        raise RuntimeError(
            f"{VENV_DIR} exists but does not contain a usable Python executable. "
            "Move or remove that directory, then rerun this setup script."
        )

    print(f"Creating dedicated standard venv at: {VENV_DIR}")
    return create_venv(explicit_python)


CHECK_CODE = f"""
import importlib

REQUIRED = {repr(REQUIRED)}
missing = []
for module_name, (package, attrs) in REQUIRED.items():
    try:
        module = importlib.import_module(module_name)
    except Exception:
        missing.append(package)
        continue
    if any(not hasattr(module, attr) for attr in attrs):
        missing.append(package)
print(",".join(missing))
"""


def missing_packages_in_env(python: Path) -> list[str]:
    output = subprocess.check_output([str(python), "-c", CHECK_CODE], text=True)
    return [item for item in output.strip().split(",") if item]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create/update the dedicated standard venv for this skill.")
    parser.add_argument(
        "--python",
        help="Optional Python 3.10+ executable used to create the venv when the default python is too old.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    python = ensure_venv(args.python)
    print(f"Using skill Python: {python}")

    missing = missing_packages_in_env(python)
    if not missing:
        print("All remote-sensing-paper-brief Python dependencies are installed in the dedicated venv.")
        return 0

    print("Missing packages:", ", ".join(missing))
    print(f"Installing from {REQUIREMENTS}")
    run([str(python), "-m", "pip", "install", "-r", str(REQUIREMENTS)])

    missing_after_install = missing_packages_in_env(python)
    if missing_after_install:
        raise RuntimeError("Packages are still missing after installation: " + ", ".join(missing_after_install))

    print("Dependencies installed.")
    print(f"Use this interpreter for skill helper scripts: {python}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
