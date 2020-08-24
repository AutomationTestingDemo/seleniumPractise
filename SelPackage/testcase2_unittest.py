import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class Test(unittest.TestCase):

    def test_goolesearch(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://mail.google.com/mail/u/0/")
        print(self.driver.title)
        self.driver.quit()

    def test_youtubesearch(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.youtube.com/")
        print(self.driver.title)
        self.driver.quit()

if __name__=="__main__":
    unittest.main()