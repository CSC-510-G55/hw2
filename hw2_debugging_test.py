"""
This module tests the merge sort algorithm.
"""

import pytest
import hw2_debugging


@pytest.mark.parametrize("input, output", [
    ([], []),
])
def test_merge_sort_empty_list(input, output):
    """Test the function with Empty Array"""
    assert hw2_debugging.merge_sort(input) == output


@pytest.mark.parametrize("input, output", [
    ([1], [1]),
])
def test_merge_sort_single_element(input, output):
    """Test the function with Single Element Array"""
    assert hw2_debugging.merge_sort(input) == output


@pytest.mark.parametrize("input, output", [
    ([5, 4, 3, 2, 1, -5, -4, -3, -2, -1], [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]),
])
def test_merge_sort_mixed_elements(input, output):
    """Test the function with Mixed Input Array"""
    assert hw2_debugging.merge_sort(input) == output
