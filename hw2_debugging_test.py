import hw2_debugging
import pytest

@pytest.mark.parametrize(
        ('input','output'),
        (
            ([],[]),
            ([1],[1]),
            ([5,4,3,2,1,-5,-4,-3,-2,-1],[-5,-4,-3,-2,-1,1,2,3,4,5])
        )
)
def test_is_prime(input, output):
    assert hw2_debugging.merge_sort(input) == output
    