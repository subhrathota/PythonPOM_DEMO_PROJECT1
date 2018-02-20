_author_ = 'subhra Thota'


import unittest
import datetime
from selenium import webdriver

class EnvironmentSetup(unittest.TestCase):

#setup contains the browser setup attributes

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Selenium\chromedriver_win32\chromedriver.exe")
        print("Test run started time" +str(datetime.datetime.now()))
        print("Chrome Environment setup...")
        print("---------------------------")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

#tear down method just to close all the browser instances and then quit

    def tearDown(self):
        if(self.driver != None):
            print("-----------------------------------------")
            print("Close the Test Environment")
            print("Run Complete at:" +str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()

