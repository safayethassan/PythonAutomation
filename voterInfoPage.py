import webDriverDetails

from webDriverDetails import *

class voterInfoClass:
#    click_on_voter_info_button = webDriverDetails.driverClass.driver.find_element_by_xpath("//div[@id='container']/div[@class='ui grid wrapper non-rounded-corners']/div[@class='top-bar']/div[@class='ui large menu topbar-desktop']/div[@class='link item']/a[@href='/nid-pub/voter-info']")

    time.sleep(3)
#    webDriverDetails.driverClass.driver.get("https://prportal.nidw.gov.bd/nid-pub/voter-info")
#    click_on_voter_info_button = webDriverDetails.driverClass.driver.find_element_by_css_selector("a[href='/nid-pub/voter-info']")

    webDriverDetails.driverClass.driver.get("dummy webpage")

    set_nid = "dummy nid"

    set_nid_input_box = webDriverDetails.driverClass.driver.find_element_by_css_selector("input[name='nid']")

    set_nid_input_box.send_keys(set_nid)

    set_day = "dummy"

    set_day_input_box = webDriverDetails.driverClass.driver.find_element_by_css_selector("input[name='day']")

    set_day_input_box.send_keys(set_day)

    set_month = "dummy"

    set_month_input_box = webDriverDetails.driverClass.driver.find_element_by_css_selector("input[name='month']")

    set_month_input_box.send_keys(set_month)

    set_year = "dummy"

    set_year_input_box = webDriverDetails.driverClass.driver.find_element_by_css_selector("input[name='year']")

    set_year_input_box.send_keys(set_year)

    time.sleep(3)

    check_voter_info_button = webDriverDetails.driverClass.driver.find_element_by_id("validate")

    check_voter_info_button.click()

