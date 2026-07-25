#!/usr/bin/env python3
"""Mirror new panache releases from PyPI as commits and tags.

For every panache-cli version on PyPI newer than the one pinned in
pyproject.toml, rewrite the pin (pyproject.toml and the `rev:` in
README.md), commit, and tag `v<version>`. Idempotent: re-running with
nothing new to mirror is a no-op.
"""

import json
import re
import subprocess
import urllib.request
from pathlib import Path

PYPROJECT = Path("pyproject.toml")
README = Path("README.md")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")


def parse(version: str) -> tuple[int, ...]:
    return tuple(int(part) for part in version.split("."))


def current_version() -> str:
    match = re.search(r'"panache-cli==([^"]+)"', PYPROJECT.read_text())
    assert match, "no panache-cli pin in pyproject.toml"
    return match.group(1)


def pypi_versions() -> list[str]:
    with urllib.request.urlopen("https://pypi.org/pypi/panache-cli/json") as response:
        releases = json.load(response)["releases"]
    versions = [
        version
        for version, files in releases.items()
        if VERSION_RE.match(version)
        and files
        and not all(f.get("yanked") for f in files)
    ]
    return sorted(versions, key=parse)


def set_version(version: str) -> None:
    pyproject = PYPROJECT.read_text()
    pyproject = re.sub(r'version = "[^"]+"', f'version = "{version}"', pyproject, count=1)
    pyproject = re.sub(r'"panache-cli==[^"]+"', f'"panache-cli=={version}"', pyproject)
    PYPROJECT.write_text(pyproject)
    README.write_text(
        re.sub(r"rev: v\d+\.\d+\.\d+", f"rev: v{version}", README.read_text())
    )


def main() -> None:
    start = parse(current_version())
    for version in pypi_versions():
        if parse(version) <= start:
            continue
        set_version(version)
        subprocess.run(["git", "add", str(PYPROJECT), str(README)], check=True)
        subprocess.run(["git", "commit", "-m", f"Mirror: v{version}"], check=True)
        subprocess.run(["git", "tag", f"v{version}"], check=True)
        print(f"mirrored v{version}")


if __name__ == "__main__":
    main()
