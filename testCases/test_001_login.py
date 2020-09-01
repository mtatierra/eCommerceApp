from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

    baseUrl = ReadConfig.getApplicationUrl()
    userName = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("************* Test_001_Login ************")
        self.logger.info("************* Verifying Homepage Title ************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************* Page Title is passed ************")
        else:
            self.logger.error("************* Page Title is failed ************")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("************* Verifying Login Page ************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("************* Login successful ************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("************* Login failed ************")
            self.driver.close()
            assert False
