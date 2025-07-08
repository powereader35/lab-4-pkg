import pytest

from geometry import shapes, utils


def test_square_area_zero_and_positive():
    a = shapes.Square(3)
    a_area = a.area()
    assert a_area == pytest.approx(9)


def test_stats_keys_and_values():
    a = shapes.Square(3)
    b = shapes.Circle(6)
    c = shapes.Square(2)

    stats = utils.area_stats((a,b,c))

    assert isinstance(stats, dict)
    expected_keys = ["n", "total", "mean", "min", "max"]
    assert set(stats.keys()) == set(expected_keys)
    assert all(isinstance(stats[key], (int, float)) for key in expected_keys)

def test_stats_raises_without_shapes():
    with pytest.raises(ValueError):
        utils.area_stats(())  
