class LoginPage:

    textBox_userName_xpath = "//input[@id='Email']"
    textBox_password_xpath = "//input[@id='Password']"
    button_login_xpath = "//input[@type = 'submit']"
    link_logout_xpath = "//a[text() = 'Logout']"

    # Implement action method for the locators
    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.textBox_userName_xpath).clear()
        self.driver.find_element_by_xpath(self.textBox_userName_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textBox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textBox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.link_logout_xpath).click()