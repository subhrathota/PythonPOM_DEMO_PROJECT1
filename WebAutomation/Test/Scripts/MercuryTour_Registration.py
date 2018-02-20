_author_ = 'Subhra Thota'

from WebAutomation.Test.PageObject.Pages.ConfirmationPage import ConfirmationPage
from WebAutomation.Test.PageObject.Pages.HomePage import Home
from WebAutomation.Test.PageObject.Pages.RegistrationPage import RegistrationPage
#from WebAutomation.Test.PageObject.Pages.SingonPage import SingonPage
from WebAutomation.Test.TestBase.EnvironmentSetup import EnvironmentSetup
from WebAutomation.Test.TestUtility.ScreenShot import SS
from selenium import webdriver
import time
import unittest

class MercuryTour_Registration(EnvironmentSetup):

    def test_RegistrationFlow(self):

        ss_path = "/Test_MercuryTours_Registration/"

        driver = self.driver
        self.driver.get("http://newtours.demoaut.com/mercurywelcome.php")
        self.driver.set_page_load_timeout(20)

        # Creating object of SS screenshots utility
        ss = SS(driver)

# Calling home page object to click on Register link
        home = Home(driver)
        if home.get_register().is_displayed():
            print("Registration Link Displayed")
            home.get_register().click()
            print("Registration Page Displayed")
            time.sleep(5)

# Calling registration page objects to continue with registration


        regist = RegistrationPage(driver)
        time.sleep(2)
        if regist.get_regis_txt().is_displayed():
            print("Registration page loaded")
            print(regist.get_regis_txt().text)
            time.sleep(6)
        else :
            print("Registration page not loaded")

        try:
            regist.setFirstName("james")
            regist.setLastName("Koney")
            regist.setPhone("07777777777")
            regist.setEmail("Test@gmail.com")
            #regist.setaddress1("4")
            #regist.setaddress2("Ealing Road")
            regist.setEmail("Ealing")
            regist.setEmail("middlesex")
            #regist.setpostcode("rgd8d4")
            regist.setCountry("UNITED KINGDOM")
            regist.setUserName("test1")
            regist.setPassword("password1")
            regist.setConfirmPassword("password1")
            time.sleep(3)
            regist.submitRegistration()
            time.sleep(4)
        except Exception as e :
            print( "Exception occured:", format(e))

# Calling post registration check

        post=ConfirmationPage(driver)
        print(post.thankyou.text)
        if (post.username_is.text).find("test1"):
            print("Registered process Successfully")
        else:
            print("Registration process not successfull")

        if __name__ == "__main__":
            unittest.main()



