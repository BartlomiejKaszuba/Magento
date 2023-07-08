# Automated system testing of an e-commerce store 'Magento'.

# Test case 10 (TC010) - reordering.

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

# Test step 1 - click on "My orders" and then "Reorder".

driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div[1]/div/div[2]/ul/li[4]/a').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="my-orders-table"]/tbody/tr[1]/td[6]/span/a[2]').click()
sleep(2)

# Test step 2 - change "Qty" and update.

# Expected result - "Grand total" is changed.

total_str = driver.find_element(By.XPATH, '//*[@id="shopping-cart-totals-table"]/tfoot/tr/td[2]').text
total_str = total_str[1:].replace('.00', '')
total_str = total_str.replace(',', '')
total = int(total_str)

qty = driver.find_element(By.XPATH, '//*[@id="shopping-cart-table"]/tbody/tr/td[4]/input')
qty.clear()
qty.send_keys('10')
driver.find_element(By.XPATH, '//*[@id="shopping-cart-table"]/tbody/tr/td[4]/button').click()
sleep(2)

new_total_str = driver.find_element(By.XPATH, '//*[@id="shopping-cart-totals-table"]/tfoot/tr/td[2]').text
new_total_str = new_total_str[1:].replace('.00', '')
new_total_str = new_total_str.replace(',', '')
new_total = int(new_total_str)

try:
    assert new_total == total * 10
    print('TC010 step 2: passed')
except AssertionError:
    print('TC010 step 2: failed')

# Test step 3 - proceed to checkout.

driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div/div/div[3]/div/ul/li[1]/button').click()
sleep(2)

# Test step 4 - complete shipping information and submit.

# Expected result - a new order number is generated.

driver.find_element(By.XPATH, '//*[@id="billing-buttons-container"]/button').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="shipping-method-buttons-container"]/button').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="dt_method_checkmo"]/label').click()
driver.find_element(By.XPATH, '//*[@id="payment-buttons-container"]/button').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="review-buttons-container"]/button').click()
sleep(2)

driver.get_screenshot_as_file('TC010.png')
driver.close()
