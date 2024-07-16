"""Dataclass and function for SVG generation."""

__author__ = "ccornix"
__copyright__ = "Copyright (c) 2024 ccornix"
__license__ = "MIT"
__all__ = ["SVGPath", "generate_svg"]

from collections.abc import Sequence
from dataclasses import dataclass
from sympy import Matrix


@dataclass(kw_only=True)
class SVGPath:
    """Representation of an SVG path."""

    points: list[Matrix]
    svg_class: list[str]

    def __str__(self) -> str:
        """Return an SVG XML string representation."""
        is_closed = self.points[-1] == self.points[0]
        if is_closed:
            points = self.points[:-1]
            suffix = " z"
        else:
            points = self.points
            suffix = ""
        points_str = " ".join(f"{float(p[0])},{float(p[1])}" for p in points)
        svg_class_str = " ".join(self.svg_class)
        return f'<path class="{svg_class_str}" d="M {points_str}{suffix}"/>'


def generate_svg(
    *,
    author: str,
    title: str,
    resolution: tuple[int, int],
    paths: Sequence[SVGPath],
) -> str:
    """Generate the SVG code of the wallpaper.

    Metadata include `author` and `title`. The CSS for styling SVG paths is
    imported from the external file at `css_path`.

    A sequence of SVG paths that compose the wallpaper are contained in
    `paths`. The desired nominal resolution of the SVG in pixels is given by
    `resolution`. This is independent of the final PNG resolution that can be a
    multiple of this nominal one.
    """
    width, height = resolution
    paths_str = "\n".join(str(path) for path in paths)
    return SVG_TEMPLATE.format(**locals())


SVG_TEMPLATE = """\
<?xml version="1.0" encoding="UTF-8"?>
<svg
  version="1.1"
  width="{width}px"
  height="{height}px"
  viewBox="0 0 {width} {height}"
  xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  xmlns:dc="http://purl.org/dc/elements/1.1/">
<title property="dc:title">{title}</title>
<desc property="dc:creator">{author}</desc>
<style type="text/css">
  .stroke {{ stroke:#202020; stroke-width:1; stroke-linecap:round; }}
  .fill-0 {{ fill:#303030; }}
  .fill-1 {{ fill:#404040; }}
  .fill-2 {{ fill:#505050; }}
</style>
<!-- Flip the y axis and move the origin to the bottom left corner -->
<g transform="translate(0,{height}) scale(1,-1)">
{paths_str}
</g>
</svg>"""
