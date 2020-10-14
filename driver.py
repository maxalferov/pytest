from appium import webdriver


class Driver:
    def __init__(self):
        desired_caps = {
            "platformName": "Android",
            "app": "/Users/alferovmaksym/Desktop/app-betabs-debug.apk",
            "deviceName": "Pixel_2_API_29",
            "appPackage": "com.upside.consumer.android.beta",
            "appActivity": "com.upside.consumer.android.activities.MainActivity"
        }

        self.instance = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
