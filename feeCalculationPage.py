import webDriverDetails

from webDriverDetails import *

class feeCalculationClass:
 #   webDriverDetails.driverClass.driver.get("dummy link")

    webDriverDetails.driverClass.driver.get("dummy link")

    time.sleep(2)

    set_nid = "dummy nid"

    set_nid_input_box = webDriverDetails.driverClass.driver.find_element_by_css_selector("input[name='nid']")

    set_nid_input_box.send_keys(set_nid)

    click_on_application_type = webDriverDetails.driverClass.driver.find_element_by_css_selector("select[name='applicationType']")

    click_on_application_type.click()

    time.sleep(2)

    click_on_both_info = webDriverDetails.driverClass.driver.find_element_by_xpath("//select[@name='applicationType']/option[@value='BOTH_INFO']")

    click_on_both_info.click()

    click_on_delivery_type = webDriverDetails.driverClass.driver.find_element_by_css_selector("select[name='deliveryType']")

    click_on_delivery_type.click()

    time.sleep(2)

    click_on_regular_smart_card = webDriverDetails.driverClass.driver.find_element_by_xpath("//select[@name='deliveryType']/option[@value='REGULAR_SMART_CARD']")

    click_on_regular_smart_card.click()

    time.sleep(2)

    check_calcualate_fee = webDriverDetails.driverClass.driver.find_element_by_id("validate")

    check_calcualate_fee.click()
