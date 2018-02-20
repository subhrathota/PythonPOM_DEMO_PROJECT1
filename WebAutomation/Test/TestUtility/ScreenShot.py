
_author_ = 'subhra thota'

from selenium import webdriver

class SS(object):

    def __init__(self, driver):
        self.driver = driver

    def ScreenShot(self,path):
        directory = "C:/Users/sujat/PycharmProjects/PythonPOM_DEMO_PROJECT/WebAutomation/ScreenShots"
        self.driver.get_screenshot_as_file(directory+path)
