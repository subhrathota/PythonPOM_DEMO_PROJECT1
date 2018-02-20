__author__ = 'Aditya Roy'

import unittest
from time import sleep
from WebAutomation.Test.PageObject.Pages.SingonPage import SignonPage
from WebAutomation.Test.TestBase.EnvironmentSetup import EnvironmentSetup
from WebAutomation.Test.PageObject.Pages.HomePage import Home
from WebAutomation.Test.TestUtility.ScreenShot import SS


class MercuryTours_SignOn(EnvironmentSetup):
    def test_SignOnPage(self):

# Screenshots relative paths
        ss_path = "/Test_MercuryTours_SignOn/"

        driver = self.driver
        self.driver.get("http://newtours.demoaut.com/")
        self.driver.set_page_load_timeout(20)
# Creating object of SS screenshots utility
        ss = SS(driver)

        home = Home(driver)
        home.signon.click()
        sleep(2)

        if driver.title == "Sign-on: Mercury Tours":
            print("Sign On page loaded successfully")
            ss.ScreenShot(ss_path+"SignOn.png")
        else:
            print("SignOn page failed to load")

        login = SignonPage(driver)
        try:
            print(login.signon_txt.get_attribute("innerText"))
            if login.regis_form.text.find("registration"):
                print("Registration link :"+login.regis_form.get_attribute("href"))

            print("Provide invalid username")
            login.signon_username.send_keys("Invalid")
            print("Provide invalid password")
            login.singon_password.send_keys("Invalid")
            ss.ScreenShot(ss_path+"InvalidID.png")
            sleep(2)
            login.submitlogin.click()
            sleep(2)
            if driver.title == "Sign-on: Mercury Tours":
                print("Invalid Credentials Provided")
                ss.ScreenShot(ss_path + "LoginDeny.png")
        except Exception as e:
            print("Exception occurred "+e)




if __name__ == '__main__':
    unittest.main()
