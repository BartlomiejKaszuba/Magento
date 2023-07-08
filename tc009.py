# Automated system testing of an e-commerce store 'Magento'.

# Test case 9 (TC009) - viewing the previous order.

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

# Test step 1 - click on "My orders" and then "View order".

# Expected result - the previous order is displayed in "Recent orders" as "Pending".

driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div[1]/div/div[2]/ul/li[4]/a').click()
sleep(2)
actual_status = driver.find_element(By.XPATH, '//*[@id="my-orders-table"]/tbody/tr[1]/td[5]').text
expected_status = 'Pending'
try:
    assert actual_status == expected_status
    print('TC009 step 1: passed')
except AssertionError:
    print('TC009 step 1: failed')

sleep(2)
driver.find_element(By.XPATH, '//*[@id="my-orders-table"]/tbody/tr[1]/td[6]/span/a[1]').click()
sleep(2)

# Test step 2 - click on "Print order".

# Expected result - the order is saved as pdf.

driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div[2]/div/div[1]/a[2]').click()
wnd = driver.window_handles
driver.switch_to.window(wnd[1])

sleep(5)
driver.quit()
