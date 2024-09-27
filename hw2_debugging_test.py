"""
This module tests the merge sort algorithm.
"""

import pytest
import hw2_debugging


@pytest.mark.parametrize("input, output", [
    ([], []),
])
def test_merge_sort_empty_list(inp, out):
    """Test the function with Empty Array"""
    assert hw2_debugging.merge_sort(inp) == out


@pytest.mark.parametrize("input, output", [
    ([1], [1]),
])
def test_merge_sort_single_element(inp, out):
    """Test the function with Single Element Array"""
    assert hw2_debugging.merge_sort(inp) == out


@pytest.mark.parametrize("input, output", [
    ([5, 4, 3, 2, 1, -5, -4, -3, -2, -1], [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]),
])
def test_merge_sort_mixed_elements(inp, out):
    """Test the function with Mixed Input Array"""
    assert hw2_debugging.merge_sort(inp) == out
