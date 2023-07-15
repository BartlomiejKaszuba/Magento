# Automated system testing of an e-commerce store 'Magento'.

# Test case 11 (TC011) - discount coupons.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Preconditions:
# The website http://live.techpanda.org/index.php/ is open.

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://live.techpanda.org/index.php/')

# Test step 1 - add an item to the cart.

driver.find_element(By.XPATH, '//*[@id="nav"]/ol/li[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div[2]'
                              '/div[1]/div[3]/ul/li[3]/div/div[3]/button').click()
sleep(2)

# Test step 2 - enter a coupon code "GURU50".

# Expected result - the price is discounted by 5%.

driver.find_element(By.ID, 'coupon_code').send_keys('GURU50')
driver.find_element(By.XPATH, '//*[@id="discount-coupon-form"]/div/div/div/div/button[1]').click()
sleep(2)
#
total_str = driver.find_element(By.XPATH, '//*[@id="shopping-cart-totals-table"]/tfoot/tr/td[2]').text
total_str = total_str[1:].replace('.00', '')
total_str = total_str.replace(',', '')
total = float(total_str)

price_str = driver.find_element(By.XPATH, '//*[@id="shopping-cart-table"]/tbody/tr/td[3]/span').text
price_str = price_str[1:].replace('.00', '')
price_str = price_str.replace(',', '')
price = float(price_str)

try:
    assert total == price * 0.95
    print('TC011 step 2: passed')
except AssertionError:
    print('TC011 step 2: failed')

driver.close()
