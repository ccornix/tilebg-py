"""Unit tests for module `lib.grid`."""

from sympy import Matrix

from tilebg.grid import generate_grid
from tilebg.path import shift
from tilebg.svg import SVGPath


def test_rectangular_grid() -> None:
    """Test path generation for a 3x3 rectangular grid with seamless style."""

    rectangle = [
        Matrix([-2, -1]),
        Matrix([2, -1]),
        Matrix([2, 1]),
        Matrix([-2, 1]),
        Matrix([-2, -1]),
    ]

    def svg_class_fn(ix: int, iy: int) -> list[str]:
        return [f"test-{(3 * iy + ix) % 4}"]

    paths = generate_grid(
        element_path=rectangle,
        spacings=(4, 2),
        resolution=(8, 4),
        offsets_fn=None,
        svg_class_fn=svg_class_fn,
    )

    assert paths == [
        # Row 0
        SVGPath(points=shift(rectangle, Matrix([0, 0])), svg_class=["test-0"]),
        SVGPath(points=shift(rectangle, Matrix([4, 0])), svg_class=["test-1"]),
        SVGPath(points=shift(rectangle, Matrix([8, 0])), svg_class=["test-0"]),
        # Row 1
        SVGPath(points=shift(rectangle, Matrix([0, 2])), svg_class=["test-3"]),
        SVGPath(points=shift(rectangle, Matrix([4, 2])), svg_class=["test-0"]),
        SVGPath(points=shift(rectangle, Matrix([8, 2])), svg_class=["test-3"]),
        # Row 2
        SVGPath(points=shift(rectangle, Matrix([0, 4])), svg_class=["test-0"]),
        SVGPath(points=shift(rectangle, Matrix([4, 4])), svg_class=["test-1"]),
        SVGPath(points=shift(rectangle, Matrix([8, 4])), svg_class=["test-0"]),
    ]
