import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
# from utilities.readProperties import ReadConfig
# from utilities.customLogger import LogGen

class Test_001_Login:
    baseurl = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    # logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        self.driver.close()
        if act_title =='Your store. Login':
            assert True
        else:
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self):
            self.driver = webdriver.Chrome()
            self.driver.get(self.baseurl)
            self.lp =Login(self.driver)
            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.ClickLogin()
            act_title =self.driver.title
            self.driver.close()
            if act_title=="Dashboard / nopCommerce administration":
                assert True
            else:
                assert False
