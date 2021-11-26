# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import webDriverDetails


for x in range(1000):


##explicit wait
 #   try:
#        element = WebDriverWait(driver, 10).until(
 #           EC.present_of_element_located((By.ID, "submit-control"))
 #       )

#    except:
#        print("failure")



    click_on_feedback_button = webDriverDetails.driverClass.driver.find_element_by_xpath("//div[@id='feedback']/a[@href='/nid-pub/feedback']")

    click_on_feedback_button.click()

    webDriverDetails.time.sleep(2)

    set_username = "Safayet Automate"

    set_mobile = "01881052953"

    set_email = "safayet_automate@gmail.com"

    set_feedback = "Safayet_Automate and 01881052953 and safayet_automate@gmail.com"

    search_username_input_box = webDriverDetails.driverClass.driver.find_element_by_css_selector("input[name='fullName']")

    search_mobile_input_box = webDriverDetails.driverClass.driver.find_element_by_css_selector("input[name='mobile']")

    search_email_input_box = webDriverDetails.driverClass.driver.find_element_by_css_selector("input[type='email'][name='email']")

    search_feedback_input_box = webDriverDetails.driverClass.driver.find_element_by_id("feedback-textarea")

    click_on_submit_button = webDriverDetails.driverClass.driver.find_element_by_id("validate")

  #  click_on_login_button = driver.find_element_by_css_selector("div[id='submit-control']")

    search_username_input_box.send_keys(set_username)

    search_mobile_input_box.send_keys(set_mobile)

    search_email_input_box.send_keys(set_email)

    search_feedback_input_box.send_keys(set_feedback)

    # time.sleep(3)

#    search_feedback_input_box.send_keys(Keys.ENTER)   ## basically input dewar pore ENTER press korar moto

    # click_on_login_button.click()

    click_on_submit_button.click()

    webDriverDetails.time.sleep(3)

    click_on_success_button = webDriverDetails.driverClass.driver.find_element_by_xpath("//div[@id='response-modal']/div[@class='actions']/div[@class='ui positive medium button']")

    click_on_success_button.click()

    webDriverDetails.time.sleep(3)

#    webDriverDetails.driverClass.driver.close()


  #  time.sleep(2)

## main = driver.find_element_by_id("main")  accessing id by main

## print(main.text) main id er moddhe thaka shob kichu k print kore dibe





## print(driver.page_source)  ##full webpage er code console e print hobe

# driver.close() #closes the window quit will terminate the driver

# See PyCharm help at https://www.jetbrains.com/help/pycharm/