import time

import webDriverDetails

from webDriverDetails import *

from selenium.webdriver.common.touch_actions import TouchActions

class makePostmanWebAutomate:
    webDriverDetails.driverClass.driver.get("https://www.postman.com/")

    time.sleep(5)

    click_on_sign_in = webDriverDetails.driverClass.driver.find_element_by_xpath("//div[@class='sc-fzokOt hLgJkJ']/div[@class='sc-AxmLO gmtmqV']/button[@type='outline']/span[@class='Button__StyledButtonText-sc-1lbqkyz-2 ipCVAL aether-button__text']")

    time.sleep(1)

    click_on_sign_in.click()

    time.sleep(5)

    set_username = "safayethassan340"

    set_password = "dagameishere11%"

    set_email_in_input_box = webDriverDetails.driverClass.driver.find_element_by_id("username")

    set_email_in_input_box.send_keys(set_username)

    set_password_in_password_box = webDriverDetails.driverClass.driver.find_element_by_id("password")

    set_password_in_password_box.send_keys(set_password)

    time.sleep(3)

    tap_on_sign_in_button = webDriverDetails.driverClass.driver.find_element_by_id("sign-in-btn")

    tap_on_sign_in_button.click()

    time.sleep(10)

    click_on_my_workspace = webDriverDetails.driverClass.driver.find_element_by_css_selector("span[title='My Workspace']")

    time.sleep(1)
    click_on_my_workspace.click()

    time.sleep(10)

    click_on_collection = webDriverDetails.driverClass.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[6]/div[1]/div[1]/div/div/div/div[1]/div[1]/div/div/div[2]/div[1]/div/div[1]/div")

    click_on_collection.click()

    time.sleep(5)

    click_on_automate_env = webDriverDetails.driverClass.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[6]/div[1]/div[1]/div/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div")

    click_on_automate_env.click()

    time.sleep(5)

    click_on_environment_field = webDriverDetails.driverClass.driver.find_element_by_css_selector("input[value='No Environment']")

    click_on_environment_field.click()

    time.sleep(2)

    click_on_test_env = webDriverDetails.driverClass.driver.find_element_by_css_selector("div[title='test']")

    click_on_test_env.click()

    time.sleep(2)

    click_on_auth_api = webDriverDetails.driverClass.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[6]/div[1]/div[1]/div/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/div/div[4]/div")

    click_on_auth_api.click()

    time.sleep(3)

    click_on_send_btn = webDriverDetails.driverClass.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[6]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[1]")

    click_on_send_btn.click()

    time.sleep(3)

    click_on_payment_api = webDriverDetails.driverClass.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[6]/div[1]/div[1]/div/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div[3]/div/div/div[4]/div")

    click_on_payment_api.click()

    time.sleep(3)

    click_on_api_body = webDriverDetails.driverClass.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[6]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/div[1]/div[1]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div/div[4]/div/span")

    click_on_api_body.click()

    time.sleep(2)

    click_on_beautify = webDriverDetails.driverClass.driver.find_element_by_css_selector("div[class='btn btn-text request-body-type-selector-beautify']")

    click_on_beautify.click()

    time.sleep(2)

    click_on_border = webDriverDetails.driverClass.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[6]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/div[1]/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[2]")

    print("border--")
    print(click_on_border)



    click_on_border.click()

    time.sleep(5)


    print("successful")

    click_on_box = webDriverDetails.driverClass.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[6]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[4]/div/div/div/div/div[1]/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[4]/div/div/div/div/div/div[1]/div[2]/div[1]/div[4]")

    click_on_box.click()

    time.sleep(5)

    print("box")

    print(click_on_box)

    click_on_json_dropdown = webDriverDetails.driverClass.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[6]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[4]/div/div/div/div/div[1]/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div/span")

#    click_on_json_dropdown.click()

    time.sleep(4)

    click_on_x_www = webDriverDetails.driverClass.driver.find_element_by_css_selector("input[value='urlencoded']")

    click_on_x_www.click()

    time.sleep(2)

    click_on_raw = webDriverDetails.driverClass.driver.find_element_by_css_selector("input[value='raw']")

    click_on_raw.click()

    time.sleep(2)

    input_body = webDriverDetails.driverClass.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[6]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/div/div/div[4]/div/div[2]/div[4]/div/div/div/div/div/div[1]/div[2]/div[1]/div[4]/div[1]")

#    set_body_transactionId =

    click_on_send = webDriverDetails.driverClass.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[6]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[1]/span")

    time.sleep(3)

    mouse_hover =webDriverDetails.driverClass.driver.find_element_by_xpath()

    mouse_hover.