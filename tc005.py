# Automated system testing of an e-commerce store 'Magento'.

# Test case 5 (TC005) - account registration.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Preconditions - the website http://live.techpanda.org/index.php/ is open.

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://live.techpanda.org/index.php/')

# Test step 1 - click on "My account" and then "Create account".

# Expected result - the account creation form is open.

driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[3]/div/div[4]/ul/li[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="login-form"]/div/div[1]/div[2]/a').click()
expected_url = 'http://live.techpanda.org/index.php/customer/account/create/'
actual_url = driver.current_url
try:
    assert actual_url == expected_url
    print('TC005 step 1: passed')
except AssertionError:
    print('TC005 step 1: failed')

# Test step 2 - fill out the form with new user data and submit.

# Expected result - account registration successful.

# Test step 2a - generating the data to put in the form with Fake Name Generator.

driver.switch_to.new_window()
driver.get('https://www.fakenamegenerator.com/')
fullname = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div'
                                         '/div[3]/div[2]/div[2]/div/div[1]').text
fullname = fullname.split('\n')[0]
firstname = fullname.split()[0]
lastname = fullname.split()[2]
email = driver.find_element(By.XPATH, '//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[9]/dd').text
email = email.split('\n')[0]
password = '1qazXSW@'

# Test step 2b - filling the registration form.

wnd = driver.window_handles
driver.switch_to.window(wnd[0])

driver.find_element(By.ID, 'firstname').send_keys(firstname)
driver.find_element(By.ID, 'lastname').send_keys(lastname)
driver.find_element(By.ID, 'email_address').send_keys(email)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.ID, 'confirmation').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button').click()
sleep(3)

# Test step 2c - verification of the welcome message.

expected_message = "WELCOME, " + firstname.upper() + " " + lastname.upper() + "!"
actual_message = driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[1]').text
try:
    assert actual_message == expected_message
    print('TC005 step 2: passed')
except AssertionError:
    print('TC005 step 2: failed')

driver.quit()

# After test - saving the email address to be re-used in other test cases.

file = open('email.txt', 'w')
file.write(email)
