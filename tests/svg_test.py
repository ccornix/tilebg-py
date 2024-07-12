"""Unit tests for module `lib.svg`."""

from pathlib import Path
from sympy import Matrix

from tilebg.svg import SVGPath, generate_svg


expected_svg = """\
<?xml version="1.0" encoding="UTF-8"?>
<svg
  version="1.1"
  width="200px"
  height="100px"
  viewBox="0 0 200 100"
  xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  xmlns:dc="http://purl.org/dc/elements/1.1/">
<title property="dc:title">title</title>
<desc property="dc:creator">author</desc>
<style type="text/css">
  .stroke { stroke:#202020; stroke-width:1; stroke-linecap:round; }
  .fill-0 { fill:#303030; }
  .fill-1 { fill:#404040; }
  .fill-2 { fill:#505050; }
</style>
<!-- Flip the y axis and move the origin to the bottom left corner -->
<g transform="translate(0,100) scale(1,-1)">
<path class="stroke fill-0" d="M -2.0,-1.0 2.0,-1.0 2.0,1.0 -2.0,1.0 z"/>
</g>
</svg>"""  # noqa: E501


def test_svg_generation() -> None:
    """Test SVG code generation featuring a single rectangular path."""
    svg = generate_svg(
        author="author",
        title="title",
        resolution=(200, 100),
        paths=[
            SVGPath(
                points=[
                    Matrix([-2, -1]),
                    Matrix([2, -1]),
                    Matrix([2, 1]),
                    Matrix([-2, 1]),
                    Matrix([-2, -1]),
                ],
                classes=["stroke", "fill-0"],
            )
        ],
    )
    assert svg == expected_svg
