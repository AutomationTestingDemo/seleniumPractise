from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
import allure
from webdriver_manager.chrome import ChromeDriverManager

# @pytest.fixture(scope='class')
# def setup():
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.maximize_window()
#     driver.implicitly_wait(20)
#     yield
#     driver.close()
#
# @pytest.mark.usefixtures('setup')
@allure.severity(allure.severity_level.NORMAL)
class TestloginORM():

    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        status = self.driver.find_element_by_xpath("//div[@id='divLogo']/img").is_displayed()
        self.driver.close()
        if status:
            assert True
        else:
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_NoOfEmp(self):
        pytest.skip("I am skipping")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.find_element_by_id('txtUsername').send_keys("Admin")
        self.driver.find_element_by_id('txtPassword').send_keys("admin123")
        self.driver.find_element_by_id('btnLogin').click()
        actTitle = self.driver.title
        if actTitle=="OrangeHRM":
            allure.attach(self.driver.get_screenshot_as_png(),name="testLoginScreen",attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False