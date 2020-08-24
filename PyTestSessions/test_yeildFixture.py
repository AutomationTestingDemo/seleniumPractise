import pytest

@pytest.fixture()
def setup():
    print("before every test")
    yield
    print("after very test")
def test1(setup):
    print("test 1")
def test2(setup):
    print("test 2")