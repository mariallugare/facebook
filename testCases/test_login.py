import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.Password()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("******Test_001_Login*****")
        self.logger.info("******Verifying Home Page Title*****")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Facebook – log in or sign up":
            assert True
            self.driver.close()
            self.logger.info("******Home Page Title test is passed*****")

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("******Verifying Home Page Title is failed*****")
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == ("(20+) Facebook"):
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login.png")
            self.driver.close()
            assert False
