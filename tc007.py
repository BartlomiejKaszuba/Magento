# Automated system testing of an e-commerce store 'Magento'.

# Test case 7 (TC007) - adding a product to the wishlist.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Preconditions:
# 1. The website http://live.techpanda.org/index.php/ is open.

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://live.techpanda.org/index.php/')

# 2. The user is logged in.

driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/a/span[2]').click()
driver.find_element(By.XPATH, '//*[@id="header-account"]/div/ul/li[6]/a').click()

file = open('email.txt', 'r')
email = file.read()
password = '1qazXSW@'

driver.find_element(By.ID, 'email').send_keys(email)
driver.find_element(By.ID, 'pass').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="send2"]').click()

# Test step 1 - open the Mobile menu.

driver.find_element(By.XPATH, '//*[@id="nav"]/ol/li[1]/a').click()

# Test step 2 - add a product to your wishlist.

# Expected result - the wishlist is updated.

driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div[2]/div[1]/'
                              'div[3]/ul/li[2]/div/div[3]/ul/li[1]/a').click()
driver.get_screenshot_as_file('TC007.png')

# Test step 3 - click on "Share wishlist".

driver.find_element(By.XPATH, '//*[@id="wishlist-view-form"]/div/div/button[1]').click()

# Test step 4 - enter an email address and submit.

# Expected result - wishlist shared successfully.

driver.find_element(By.ID, 'email_address').send_keys('bk0628@mailinator.com')
driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button').click()
sleep(2)

actual_message = driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]'
                                               '/div/div[2]/div/div[1]/ul/li/ul/li').text
expected_message = 'Your Wishlist has been shared.'

try:
    assert actual_message == expected_message
    print('TC007 step 4: passed')
except AssertionError:
    print('TC007 step 4: failed')

driver.close()
