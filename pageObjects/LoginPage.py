import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//button[contains(text(),'Log in')]"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUsername (self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        time.sleep(2)
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setPassword (self,Password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        time.sleep(2)
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(Password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def ClickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()