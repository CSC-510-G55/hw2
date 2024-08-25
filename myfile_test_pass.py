import myfile
import pytest

@pytest.mark.parametrize(
        ('input','output'),
        (
            (0,False),
            (1,False),
            (5,True)
        )
)
def test_is_prime(input, output):
    assert myfile.is_prime(input) == output
    