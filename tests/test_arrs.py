from utils.arrs import get_, my_slice
from utils import arrs
import pytest


def test_get():
    assert get_([1, 2, 3], 1, "test") == 2
    assert get_([], 0, "test") == "test"
    assert arrs.get([1, 2, 3, 4, 5], 2) == 3
    assert arrs.get([1, 2, 3, 4, 5], 10, default="Not found") == "Not found"
    assert arrs.get([1, 2, 3, 4, 5], 3) != 5
    assert arrs.get([1, 2, 3, 4, 5], -1) == 5
    assert arrs.get([], 0, default="Empty") == "Empty"
    assert arrs.get([1, 2, 3, 4, 5], 3) == int("4")


def test_slice():
    assert my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5]) != [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], 2) == [3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], end=3) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], start=-3, end=-1) == [3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], start=2) == [3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], end=2) == [1, 2]
    assert arrs.my_slice([1, 2, 3, 4, 5], start=-3, end=-2) == [3]
    assert arrs.my_slice([1, 2, 3, 4, 5], start=-5, end=5) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4, 5]) != []

