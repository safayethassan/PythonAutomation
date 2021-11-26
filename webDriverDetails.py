from telnetlib import EC

from selenium.webdriver.support import expected_conditions as EC

import  selenium

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.webdriver import ChromeRemoteConnection

from selenium.webdriver.firefox.webdriver import FirefoxBinary

from selenium.webdriver.firefox.webdriver import FirefoxProfile

from selenium.webdriver.firefox.webdriver import FirefoxWebElement

from selenium.webdriver.firefox.webdriver import FirefoxRemoteConnection

from selenium.webdriver.common.desired_capabilities import *

from selenium.webdriver.common.action_chains import *

from selenium.webdriver.common.touch_actions import *

from selenium.webdriver.common.utils import *

from selenium.webdriver.common.alert import *

from selenium.webdriver.common.service import *

from select import select

import time

from selenium.webdriver.support.wait import WebDriverWait

Chrome_PATH = "G:\chromedriver_win32\chromedriver.exe"  #nijer moto path set kore nite hobe
Firefox_PATH = "G:\geckodriver-v0.30.0-win64\geckodriver.exe"

class driverClass:
    driver = webdriver.Chrome(Chrome_PATH)

    driver.maximize_window()

#    driver.get("https://prportal.nidw.gov.bd/nid-pub/")

#    driver.get("http://localhost:8080/nid-pub")



    time.sleep(2)