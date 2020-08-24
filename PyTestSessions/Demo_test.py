import pytest

def test_m1():
    a=3
    b=4
    assert a+1==b, "Test Passed"
    assert a==b,"Test Failed"
@pytest.mark.login
def test_m2():
    a="kalyan"
    b="kalyan"
    assert a==b
def test_m3():
    assert True
@pytest.mark.login
def test_m4():
    assert False
@pytest.mark.login
def test_m5():
    name="selenium"
    assert name.upper()=="SELENIUM"
