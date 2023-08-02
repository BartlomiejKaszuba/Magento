# Automated system testing of an e-commerce store 'Magento'.

# Test case 12 (TC012) - advanced search.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Preconditions - the website http://live.techpanda.org/index.php/ is open.

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://live.techpanda.org/index.php/')

# Test step 1 - open "Advanced search".

driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[3]/div/div[3]/ul/li[3]/a').click()

# Test step 2 - enter any price range.

# Expected result - products within the specified price range are displayed.

price_from = driver.find_element(By.XPATH, '//*[@id="price"]')
price_from.send_keys('0')
price_to = driver.find_element(By.XPATH, '//*[@id="price_to"]')
price_to.send_keys('150')
driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button').click()
sleep(3)
prices = driver.find_elements(By.XPATH, '//*[contains(@class, "-price")]')
for price in prices:
    price_str = price.text
    price_str1 = price_str.replace('.00', '')
    price_str2 = price_str1.replace('$', '')
    price_int = int(price_str2)
    print(price_int)
    try:
        assert 0 <= price_int <= 150
    except AssertionError:
        print('TC012 step 2: failed')

# Test step 3 - enter a different price range.

# Expected result - products within the specified price range are displayed.

driver.back()
sleep(2)
price_from = driver.find_element(By.XPATH, '//*[@id="price"]')
price_from.clear()
price_from.send_keys('200')
price_to = driver.find_element(By.XPATH, '//*[@id="price_to"]')
price_to.clear()
price_to.send_keys('1000')
driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button').click()
sleep(3)
prices = driver.find_elements(By.XPATH, '//*[contains(@class, "-price")]')
for price in prices:
    price_str = price.text
    price_str1 = price_str.replace('.00', '')
    price_str2 = price_str1.replace('$', '')
    price_int = int(price_str2)
    print(price_int)
    try:
        assert 200 <= price_int <= 1000
    except AssertionError:
        print('TC012 step 3: failed')

driver.close()
