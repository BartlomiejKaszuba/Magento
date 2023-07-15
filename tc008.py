# Automated system testing of an e-commerce store 'Magento'.

# Test case 8 (TC008) - purchasing a product.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

# Test step 1 - click on "My wishlist".

driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div[1]/div/div[2]/ul/li[8]/a').click()
sleep(5)

# Test step 2 - add the product to cart and proceed to checkout.

driver.find_element(By.XPATH, '//*[@title="Add to Cart"]').click()
sleep(5)
driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div/div/div[1]/ul/li/button').click()

# Test step 3 - enter shipping information and click "Estimate".

# Expected result - the shipping cost of $5 is generated.

address = '4036 Short Street'
city = 'New York'
postcode = '542896'
phone = '123456789'

driver.find_element(By.ID, 'billing:street1').send_keys(address)
driver.find_element(By.ID, 'billing:city').send_keys(city)
select = Select(driver.find_element(By.ID, 'billing:region_id'))
select.select_by_visible_text(city)
driver.find_element(By.ID, 'billing:postcode').send_keys(postcode)
driver.find_element(By.ID, 'billing:telephone').send_keys(phone)
driver.find_element(By.XPATH, '//*[@id="billing-buttons-container"]/button').click()
driver.execute_script("window.scrollTo(0,0)")
sleep(2)
rate = driver.find_element(By.XPATH, '//*[@id="checkout-shipping-method-load"]/dl/dd/ul/li/label').text
try:
    assert '$5' in rate
    print('TC008 step 3: passed')
except AssertionError:
    print('TC008 step 3: failed')

# Test step 4 - proceed to the payment method, select "Check/money order", and continue.

# Expected result - the shipping cost is added to the product cost.

driver.find_element(By.XPATH, '//*[@id="shipping-method-buttons-container"]/button').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="dt_method_checkmo"]/label').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="payment-buttons-container"]/button').click()
sleep(2)

total_str = driver.find_element(By.XPATH, '//*[@id="checkout-review-table"]/tfoot/tr[3]/td[2]').text
total = int(total_str[1:4])
subtotal_str = driver.find_element(By.XPATH, '//*[@id="checkout-review-table"]/tfoot/tr[1]/td[2]').text
subtotal = int(subtotal_str[1:4])
try:
    assert total == subtotal + 5
    print('TC008 step 4: passed')
except AssertionError:
    print('TC008 step 4: failed')

# Test step 5 - place the order.

# Expected result - the order is placed, a number is generated.

driver.find_element(By.XPATH, '//*[@id="review-buttons-container"]/button').click()
sleep(2)
driver.get_screenshot_as_file('TC008.png')

driver.close()
