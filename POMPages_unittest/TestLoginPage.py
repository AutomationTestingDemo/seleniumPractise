from selenium import webdriver
class LoginPage():
    userNameTextbox_id="Email"
    passwordTextbox_id='Password'
    loginButton_xpath="//input[@type='submit']"
    logoutButton_xpath = "//a[text()='Logout']"

    def __init__(self,driver):
        self.driver = driver
    def enterUsername(self,username):
        u = self.driver.find_element_by_id(self.userNameTextbox_id)
        u.clear()
        u.send_keys(username)
    def enterPassword(self,password):
        p = self.driver.find_element_by_id(self.passwordTextbox_id)
        p.clear()
        p.send_keys(password)
    def clickLoginbutton(self):
        self.driver.find_element_by_xpath(self.loginButton_xpath).click()
    def clickLogoutButton(self):
        self.driver.find_element_by_xpath(self.logoutButton_xpath).click()