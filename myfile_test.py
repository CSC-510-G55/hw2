import myfile
import pytest

@pytest.mark.parametrize(
        ('input','output'),
        (
            (9,False),
            (1,True),
        )
)
def test_is_prime(input, output):
    assert myfile.is_prime(input) == output
    