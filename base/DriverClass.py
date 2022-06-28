from appium import webdriver


class Driver:

    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'Redmi'
        desired_caps['app'] = ('C:/Users/ajinkyas.shukla_info/Desktop/Appium/General_Store.apk')
        desired_caps['appWaitPackage'] = 'com.androidsample.generalstore'
        desired_caps['appWaitActivity'] = 'com.androidsample.generalstore.MainActivity'
        desired_caps['noReset'] = True

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver

