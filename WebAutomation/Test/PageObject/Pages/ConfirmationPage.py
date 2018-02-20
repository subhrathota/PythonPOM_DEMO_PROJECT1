_author_ = 'subhra Thota'


from WebAutomation.Test.PageObject.Locators import Locator
from selenium.webdriver.support.select import  Select
from selenium.webdriver.common.by import By
from selenium import webdriver

class ConfirmationPage(object):

    def __init__(self,driver):
        self.driver = driver

# Registration page locators

        self.thankyou = driver.find_element(By.XPATH, Locator.thank_you)
        self.username_is = driver.find_element(By.XPATH,Locator.username_is)

    def get_thankyou(self):
        return self.thankyou

    def get_username_is(self):
        return self.username_is