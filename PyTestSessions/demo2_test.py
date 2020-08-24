import pytest
@pytest.mark.login
def test_m6():
    name="selenium"
    assert name.upper()=="SELENIUM"