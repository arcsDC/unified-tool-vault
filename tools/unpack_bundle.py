#!/usr/bin/env python3
import json
import sys
from pathlib import Path, PurePosixPath


def safe_path(root: Path, relative: str) -> Path:
    pure = PurePosixPath(relative)
    if not relative or any(part in {"", ".", ".."} for part in pure.parts):
        raise ValueError(f"Unsafe path in bundle: {relative!r}")
    target = root.joinpath(*pure.parts)
    target.parent.mkdir(parents=True, exist_ok=True)
    return target


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: unpack_bundle.py <bundle.json> <output-directory>")

    bundle_path = Path(sys.argv[1])
    output = Path(sys.argv[2])
    bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
    files = bundle.get("files", {})

    if not isinstance(files, dict):
        raise ValueError("Bundle files field must be an object.")

    output.mkdir(parents=True, exist_ok=True)
    for relative, content in files.items():
        if not isinstance(relative, str) or not isinstance(content, str):
            raise ValueError("Invalid file entry in bundle.")
        safe_path(output, relative).write_text(content, encoding="utf-8")

    print(f"Restored {len(files)} files into {output}")


if __name__ == "__main__":
    main()
