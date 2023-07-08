# Automated system testing of an e-commerce store 'Magento'.

# Test case 6 (TC006) - account registration.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Preconditions - the website http://live.techpanda.org/index.php/ is open.

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://live.techpanda.org/index.php/')

# Test step 1 - click on "Account" and then "Log In".

# Expected result - the login page is open.

driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/a/span[2]').click()
driver.find_element(By.XPATH, '//*[@id="header-account"]/div/ul/li[6]/a').click()

expected_url = 'http://live.techpanda.org/index.php/customer/account/login/'
actual_url = driver.current_url
try:
    assert actual_url == expected_url
    print('TC006 step 1: passed')
except AssertionError:
    print('TC006 step 1: failed')

# Test step 2 - log in with the previously used email address and password.

# Expected result - login successful.

file = open('email.txt', 'r')
email = file.read()
password = '1qazXSW@'

driver.find_element(By.ID, 'email').send_keys(email)
driver.find_element(By.ID, 'pass').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="send2"]').click()

sleep(2)
driver.get_screenshot_as_file('TC006.png')
driver.close()
