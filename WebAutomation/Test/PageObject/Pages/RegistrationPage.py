_author_ = 'subhra Thota'


from WebAutomation.Test.PageObject.Locators import Locator
from selenium.webdriver.support.select import  Select
from selenium.webdriver.common.by import By
from selenium import webdriver

class RegistrationPage(object):

    def __init__(self,driver):
        self.driver = driver

# Registration page locators

        self.regis_txt = driver.find_element(By.XPATH,Locator.regis_text)
        self.firstname = driver.find_element(By.XPATH, Locator.firstname)
        self.lastname = driver.find_element(By.XPATH,Locator.lastname)
        self.phone = driver.find_element(By.XPATH, Locator.phone)
        self.email = driver.find_element(By.XPATH,Locator.email)
        self.country = driver.find_element(By.XPATH,Locator.country)
        self.username = driver.find_element(By.XPATH,Locator.username)
        self.password = driver.find_element(By.XPATH,Locator.password)
        self.confirmpassword = driver.find_element(By.XPATH,Locator.confirmpassword)
        self.submit = driver.find_element(By.XPATH,Locator.submit)

# You can return the web element by method and you can call it also, and useful method  with parameter you define here

    def get_regis_txt(self):
        return self.regis_txt

    def setFirstName(self, Name):
        self.firstname.clear()
        self.firstname.send_keys(Name)

    def setLastName(self, Name):
        self.lastname.clear()
        self.lastname.send_keys(Name)

    def setPhone(self, phone):
        self.phone.clear()
        self.phone.send_keys(phone)

    def setEmail(self, email):
        self.email.clear()
        self.email.send_keys(email)

    def setCountry(self, country):
        select = Select(self.country)
        select.select_by_visible_text(country)

    def setUserName(self, userName):
        self.username.clear()
        self.username.send_keys(userName)

    def setPassword(self, password):
        self.password.clear()
        self.password.send_keys(password)

    def setConfirmPassword(self, confirmPassword):
        self.confirmpassword.clear()
        self.confirmpassword.send_keys(confirmPassword)

    def submitRegistration(self):
        self.submit.click()






