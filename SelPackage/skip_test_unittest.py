import unittest

class Apptesting(unittest.TestCase):
    def test_google(self):
        print("Login google")
    @unittest.skipIf(1!=2,"1 is not equal to 2")
    def test_facebook(self):
        print("Login facebook")
    def test_youtube(self):
        print("Login youtube")
    def test_twitter(self):
        print("Login twitter")
    @unittest.skip("Safari is boring")
    def test_safari(self):
        print("Login safari")
    @unittest.SkipTest #decorator
    def test_firefox(self):
        print("Login firefox")
# if __name__=="__main__":
#     unittest.main()
