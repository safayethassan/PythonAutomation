import select

from loginPage import loginPageClass

import string

from loginPage import *

from webDriverDetails import *

click_on_profile_details = webDriverDetails.driverClass.driver.find_element_by_css_selector("div[class='ui big button view-profile']")

print(click_on_profile_details)

click_on_profile_details.click()

webDriverDetails.time.sleep(3)

click_on_edit_button = webDriverDetails.driverClass.driver.find_element_by_xpath("//div[@class='right floated right aligned six wide column button-group-one mobile']/a[@id='edit']/div[@class='ui popup-button big button']")

click_on_edit_button.click()

webDriverDetails.time.sleep(1)

click_on_continue_button = webDriverDetails.driverClass.driver.find_element_by_xpath("//div[@id='modal']/div[@class='actions']/div[@class='ui positive right labeled icon button']")

click_on_continue_button.click()

webDriverDetails.time.sleep(3)

click_on_blood_group_checkbox = webDriverDetails.driverClass.driver.find_element_by_xpath("//form[@id='form']/div[@data-tab='first']/div[@class='ui stackable grid']/div[@class='row']/div[@class='twelve wide column']/div[@class='ui three column grid vertically padded grid stackable']/div[@class='column field']/label/input[@class='select-field']")

click_on_blood_group_checkbox.click()

webElement = webDriverDetails.driverClass.driver.find_element_by_css_selector("select[name='bloodGroup']").get_attribute("value")

print(webElement)

click_on_blood_group_level = webDriverDetails.driverClass.driver.find_element_by_css_selector("select[name='bloodGroup']")

#click_on_blood_group_level.click()

if(webElement == "A+"):
    select_blood_group_as_B = webDriverDetails.driverClass.driver.find_element_by_xpath("//select[@name='bloodGroup']/option[@value='B-']")
    select_blood_group_as_B.click()

else:
    select_blood_group_as_A = webDriverDetails.driverClass.driver.find_element_by_xpath("//select[@name='bloodGroup']/option[@value='A+']")
    select.select(select_blood_group_as_A)

click_on_next_button = webDriverDetails.driverClass.driver.find_element_by_id("next-type")

click_on_next_button.click()

webDriverDetails.time.sleep(2)

click_on_next_transaction = webDriverDetails.driverClass.driver.find_element_by_id("next-transaction")

click_on_next_transaction.click()

webDriverDetails.time.sleep(2)

