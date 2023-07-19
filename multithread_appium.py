from threading import Thread
from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess


def login_to_spotify(instance_port, udid):
    adb_command = f"adb connect {udid}"
    process = subprocess.Popen(adb_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        print(f"Error connecting to adb instance {udid}: {error}")
        return

    appium_service = AppiumService()
    appium_service.start(args=['--address', '127.0.0.1', '--port', str(instance_port),'-pa' ,'/wd/hub'])
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '9',
        'automationName' : 'UiAutomator2',
        'udid':str(udid),
        "appPackage": "com.spotify.music",
        "appActivity": "com.spotify.music.MainActivity",
        "app": "C:\\Users\\okthi\\Downloads\\Spotify v8.8.44.527 [Premium].apk"
    }

    driver = webdriver.Remote(f'http://127.0.0.1:{instance_port}/wd/hub', desired_caps)
    wait = WebDriverWait(driver, 30)
    # create a new instance of the driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    wait = WebDriverWait(driver, 30)

    ###click log in
    element = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.Button[4]')))
    # click on the element
    element.click()

    ###type username
    element = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText')))
    # click on the element
    element.send_keys("email")

    ###type password
    element = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText')))
    # click on the element
    element.send_keys("pass")

    ###log in
    element = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.Button[1]')))
    # click on the element
    element.click()

    #end of the process
    appium_service.stop()


# Create threads for each instance

number_of_instances = 2
threads = []
for i in range(number_of_instances):
    instance_port = 4723 + i   # Assuming each instance runs on a different port
    udid = "127.0.0.1:"+str(5555 + (i * 10))  # Assuming each instance runs on a different port
    thread = Thread(target=login_to_spotify, args=(instance_port, udid))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()
