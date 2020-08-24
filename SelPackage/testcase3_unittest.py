import unittest

def setUpModule():
    print("Before Module")

def tearDownModule():
    print("Teardown module")

class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("Login Script")

    def test1(self):
        print("hello1")

    def test2(self):
        print("hello2")

    def test3(self):
        print("hello3")

    def test4(self):
        print("hello4")

    @classmethod
    def tearDown(self):
        print("tear down")

    @classmethod
    def setUpClass(cls):
        print("setupclass")

    @classmethod
    def tearDownClass(cls):
        print("Teardown class")