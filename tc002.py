# Automated system testing of an e-commerce store 'Magento'.

# Test case 2 (TC002) - product cost verification.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Preconditions - the website http://live.techpanda.org/index.php/ is open.

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://live.techpanda.org/index.php/')

# Test step 1 - open the Mobile menu.

driver.find_element(By.XPATH, '//*[@id="nav"]/ol/li[1]/a').click()

# Test step 2 - read the cost of Sony Xperia.

cost_menu = driver.find_element(By.XPATH, '//*[@id="product-price-1"]/span').text

# Test step 3 - open the Sony Xperia detail page.

driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[1]/div/h2/a').click()

# Test step 4 - read the cost of Sony Xperia from the detail page and compare the two values.

# Expected result - the prices in the Mobile menu and the detail page should be equal.

cost_dp = driver.find_element(By.XPATH, '//*[@id="product-price-1"]/span').text
try:
    assert cost_dp == cost_menu
    print('TC002 step 4: passed')
except AssertionError:
    print('TC002 step 4: failed')

driver.close()
