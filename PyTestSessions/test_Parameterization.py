import pytest

@pytest.mark.parametrize("num",(1,2))
def test_calculation(num):
    print("Number is :",num)