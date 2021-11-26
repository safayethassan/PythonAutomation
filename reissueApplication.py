import select

from loginPage import loginPageClass

import string

from loginPage import *

from webDriverDetails import *

click_on_reissue_tab = webDriverDetails.driverClass.driver.find_element_by_xpath("//div[@id='top-menu']/a[@href='/nid-pub/citizen-home/reissue/']")

click_on_reissue_tab.click()

webDriverDetails.time.sleep(2)

click_on_edit_button = webDriverDetails.driverClass.driver.find_element_by_xpath("//a[@id='edit']/div[@class='ui popup-button big button']")

click_on_edit_button.click()

webDriverDetails.time.sleep(1)

click_on_continue_button = webDriverDetails.driverClass.driver.find_element_by_xpath("//div[@id='modal']/div[@class='actions']/div[@class='ui positive right labeled icon button']")

click_on_continue_button.click()

click_on_reissue_dropdown = webDriverDetails.driverClass.driver.find_element_by_xpath("//select[@name='reprintReason']")

click_on_reissue_dropdown.click()

click_on_lost_cause = webDriverDetails.driverClass.driver.find_element_by_xpath("//select[@name='reprintReason']/option[@value='LOST']")

click_on_lost_cause.click()

webDriverDetails.time.sleep(1)

click_on_next_transaction = webDriverDetails.driverClass.driver.find_element_by_id("next-transaction")

webDriverDetails.time.sleep(3)

