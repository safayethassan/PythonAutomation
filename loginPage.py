# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import webDriverDetails
from webDriverDetails import *
class loginPageClass:

    ##explicit wait
    #   try:
    #        element = WebDriverWait(driver, 10).until(
    #           EC.present_of_element_located((By.ID, "submit-control"))
    #       )

    #    except:
    #        print("failure")

    time.sleep(3)

    set_username = "testrafa1"

    set_password = "123456"

    search_username_input_box = webDriverDetails.driverClass.driver.find_element_by_css_selector("input[name='username']")

    search_user_password_input_box = webDriverDetails.driverClass.driver.find_element_by_css_selector("input[type='password'][name='password']")

    click_on_login_button = webDriverDetails.driverClass.driver.find_element_by_css_selector("div[id='submit-control']")

    search_username_input_box.send_keys(set_username)

    search_user_password_input_box.send_keys(set_password)

    time.sleep(3)

    search_user_password_input_box.send_keys(Keys.ENTER)  ## basically input dewar pore ENTER press korar moto

    # click_on_login_button.click()

    time.sleep(5)

    ## main = driver.find_element_by_id("main")  accessing id by main

    ## print(main.text) main id er moddhe thaka shob kichu k print kore dibe

    ## print(driver.page_source)  ##full webpage er code console e print hobe

    # driver.close() #closes the window quit will terminate the driver

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

