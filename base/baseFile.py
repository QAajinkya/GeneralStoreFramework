import allure
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import utilities.CustomLogger as cl
import time


class BasePage:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorValue, locatorType):
        locatorType = str(locatorType).lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locatorType == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locatorValue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorValue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                         'UiSelector().description("%s")' % locatorValue))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(%d)" % int(locatorValue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % locatorValue))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '%s' % locatorValue))
            return element
        else:
            self.log.info("Locator value " + locatorValue + "not found")

        return element

    def getElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info("Element found with locatorType:" + locatorType + "with the locator value: " + locatorValue)
        except:
            self.log.info(
                "Element not found with locatorType:" + locatorType + "with the locator value: " + locatorValue)

            self.takeScreenShot(locatorType)
            assert False

        return element

    def clickElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info(
                "Clicked on element found with locatorType: " + locatorType + "with the locator value: " + locatorValue)
        except:
            self.log.info(
                "Unable to click on element not found with locatorType: " + locatorType + "with the locator value: " + locatorValue)

            self.takeScreenShot(locatorType)
            assert False

    def sendText(self, text, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Send text on element found with locatorType: " + locatorType + "with the locator value: " + locatorValue)
        except:
            self.log.info(
                "Unable to Send text on element not found with locatorType: " + locatorType + "with the locator value: " + locatorValue)

            self.takeScreenShot(locatorType)
            assert False  # this asserts tell that testcase has failed if we don't write this will pass the TC

    def isDisplayed(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info(
                "Element found with locatorType: " + locatorType + "with the locator value: " + locatorValue + "is displayed")
            return True

        except:
            self.log.info(
                "Element not found with locatorType: " + locatorType + "with the locator value: " + locatorValue + "is not displayed")

            self.takeScreenShot(locatorType)
            assert True

            return False

    def Screenshot(self, screeshotName):
        fileName = screeshotName + "_" + (
            time.strftime("%d_%m_%y_%H_M_S")) + ".png"  # what format we want to save the screenshots
        screenshotDirectory = "../reports/screenshots/"  # folder where we want to save the screenshots
        screenshotPath = screenshotDirectory + fileName  # this gives path to the directory
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to path : " + screenshotPath)
        except:
            self.log.info("Unable to save the Screenshot to the path : " + screenshotPath)

    def takeScreenShot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotIssue", attachment_type=AttachmentType.PNG)

    def keyCode(self, value):
        self.driver.press_keycode(value)
