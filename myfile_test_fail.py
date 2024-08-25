import myfile
import pytest

@pytest.mark.parametrize(
        ('input','output'),
        (
            (1,True),
            (-1,True)
        )
)
def test_is_prime(input, output):
    assert myfile.is_prime(input) == output
    