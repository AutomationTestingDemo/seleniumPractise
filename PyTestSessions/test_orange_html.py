from selenium import webdriver
import unittest
import HtmlTestRunner
from webdriver_manager.chrome import ChromeDriverManager

class Orange(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
    def testveriyTitle(self):
        self.driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
        assert self.driver.title =='Free Human Resource Management Software | 30 Day Trial Creation','This test is passed'
        print(self.driver.title)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\PyTestSessions'))
