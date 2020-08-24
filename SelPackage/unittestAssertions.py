import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class Test(unittest.TestCase):
    def testAssertions(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.google.com/")
        self.assertEqual()
        self.assertNotEqual()
        self.assertTrue()
        self.assertFalse()
        self.assertIsNone()
        self.assertIsNotNone()
        self.assertIn("value","checks the value is present in list")
        self.assertNotIn("value","checks the value is not present in list")
