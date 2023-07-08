# Automated system testing of an e-commerce store 'Magento'.

# Test case 3 (TC003) - verify that you cannot add more product to cart than available in store.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Preconditions - the website http://live.techpanda.org/index.php/ is open.

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://live.techpanda.org/index.php/')

# Test step 1 - open the Mobile menu.

driver.find_element(By.XPATH, '//*[@id="nav"]/ol/li[1]/a').click()

# Test step 2 - click 'Add to cart' for Sony Xperia.

driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div[2]'
                              '/div[1]/div[3]/ul/li[1]/div/div[3]/button/span/span').click()

# Test step 3 - change 'Qty' to 1000 and update.

# Expected result - an error message 'The requested quantity for "Sony Xperia" is not available.' should be displayed.

qty = driver.find_element(By.XPATH, '//*[@id="shopping-cart-table"]/tbody/tr/td[4]/input')
qty.clear()
qty.send_keys(1000)
driver.find_element(By.XPATH, '//*[@id="shopping-cart-table"]/tbody/tr/td[4]/button/span/span').click()
driver.implicitly_wait(3)

expected_text = 'The requested quantity for "Sony Xperia" is not available.'
actual_text = driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div/div/ul/li/ul/li').text
try:
    assert expected_text == actual_text
    print('TC003 step 3: passed')
except AssertionError:
    print('TC003 step 3: failed')

# Test step 4 - click 'Empty cart'.

# Expected result - a message 'SHOPPING CART IS EMPTY' should be displayed.

driver.find_element(By.ID, 'empty_cart_button').click()
expected_message = 'SHOPPING CART IS EMPTY'
actual_message = driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div/div[1]').text
try:
    assert expected_message == actual_message
    print('TC003 step 4: passed')
except AssertionError:
    print('TC003 step 4: failed')

driver.close()
