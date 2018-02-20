_author_ = 'subhra Thota'


from WebAutomation.Test.PageObject.Locators import Locator
from selenium.webdriver.support.select import  Select
from selenium.webdriver.common.by import By
from selenium import webdriver

class SignonPage(object):

    def __init__(self,driver):
        self.driver = driver

# Registration page locators

        self.signon_username = driver.find_element(By.XPATH, Locator.signon_username)
        self.singon_password = driver.find_element(By.XPATH,Locator.signon_password)
        self.submitlogin = driver.find_element(By.XPATH, Locator.submitlogin)
        self.signon_txt = driver.find_element(By.XPATH,Locator.signon_txt)
        self.regis_form = driver.find_element(By.XPATH, Locator.regis_form)

    def get_signon_username(self):
        return self.signon_username

    def get_signon_passeord(self):
        return self.singon_password

    def get_submitlogin(self):
        return self.submitlogin

    def get_signon_txt(self):
        return self.signon_txt

    def get_regis_from(self):
        return self.regis_form