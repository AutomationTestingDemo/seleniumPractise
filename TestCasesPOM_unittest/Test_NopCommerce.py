import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys
sys.path.append("C:/Selenium_Python")
from POMPages_unittest.TestLoginPage import LoginPage

class LoginTest(unittest.TestCase):
    baseUrl = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password='admin'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(20)

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseUrl)
    def test_login(self):
        lp = LoginPage(self.driver)
        lp.enterUsername(self.username)
        lp.enterPassword(self.password)
        lp.clickLoginbutton()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration",self.driver.title,"This Testcase is passed")
        lp.clickLogoutButton()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..\\POMReports"))