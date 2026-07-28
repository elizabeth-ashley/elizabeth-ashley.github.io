#!/usr/bin/env python
"""Compile _scss/main.scss -> css/main.css.

Stands in for the `gulp styles` task, which no longer runs: gulp-sass@4 depends
on node-sass, and the pinned Node (.nvmrc, v10.13.0) has been EOL since 2021.

This uses libsass via the `sass` Python package, so it needs no Node at all:

    pip install libsass
    python _scripts/build_css.py            # compressed, as gulp emitted
    python _scripts/build_css.py --expanded # readable, for debugging

Note: the old pipeline also ran gulp-autoprefixer. libsass does not prefix, so
anything needing vendor prefixes must be written out explicitly in the SCSS.
The v2026 partials use grid, flexbox and custom properties, all of which are
unprefixed in every browser this site targets.
"""

import argparse
import pathlib
import sys

try:
    import sass
except ImportError:
    sys.exit("libsass is not installed. Run: pip install libsass")

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "_scss" / "main.scss"
OUT = ROOT / "css" / "main.css"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--expanded", action="store_true",
                        help="emit readable CSS instead of compressed")
    args = parser.parse_args()

    if not SRC.exists():
        sys.exit(f"missing source: {SRC}")

    try:
        css = sass.compile(
            filename=str(SRC),
            output_style="expanded" if args.expanded else "compressed",
            include_paths=[str(ROOT / "_scss")],
        )
    except sass.CompileError as exc:
        sys.exit(f"SASS COMPILE FAILED\n{exc}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(css, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}  ({len(css):,} bytes)")


if __name__ == "__main__":
    main()
