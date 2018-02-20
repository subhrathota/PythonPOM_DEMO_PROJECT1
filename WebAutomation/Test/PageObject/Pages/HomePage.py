import self as self

_author_ = 'subhra thota'

from WebAutomation.Test.PageObject.Locators import Locator
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver

class Home(object):

    def __init__(self,driver):
        self.driver = driver

# initialising the home locators

        self.logo = driver.find_element(By.XPATH, Locator.logo)
        self.signon = driver.find_element(By.XPATH,Locator.singon)
        self.register = driver.find_element(By.XPATH,Locator.register)
        self.support = driver.find_element(By.XPATH,Locator.support)
        self.contact = driver.find_element(By.XPATH,Locator.contact)


    def get_logo(self):
        return self.logo
        #print(driver.find_element(By.XPATH, Locator.logo))

    def get_signon(self):
        return self.signon

    def get_register(self):
        return self.register
       #print(self.register)

    def get_support(self):
        return self.support

    def get_contact(self):
        return self.contact




