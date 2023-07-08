# Automated system testing of an e-commerce store 'Magento'.

# Test case 4 (TC004) - product comparison.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Preconditions - the website http://live.techpanda.org/index.php/ is open.

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://live.techpanda.org/index.php/')

# Test step 1 - open the Mobile menu.

driver.find_element(By.XPATH, '//*[@id="nav"]/ol/li[1]/a').click()

# Test step 2 - click on "Add to compare" for 2 mobiles.

driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div[2]/'
                              'div[1]/div[3]/ul/li[1]/div/div[3]/ul/li[2]/a').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div[2]/'
                              'div[1]/div[3]/ul/li[3]/div/div[3]/ul/li[2]/a').click()
sleep(2)

# Test step 3 - click on the "Compare" button.

# Expected result - A popup window with a product comparison with a heading "COMPARE PRODUCTS" is displayed.

driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div[3]/div[1]/div[2]/div/button').click()
wnd = driver.window_handles
driver.switch_to.window(wnd[1])
expected_title = "COMPARE PRODUCTS"
actual_title = driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div[1]').text
try:
    assert actual_title.startswith(expected_title)
    print('TC004 step 3: passed')
except AssertionError:
    print('TC004 step 3: failed')
    print(actual_title)

# Test step 4 - close the popup window.

# Expected result - the popup window is closed.

driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div[2]/button').click()
wnd = driver.window_handles
if len(wnd) == 1:
    print('TC004 step 4: passed')
else:
    print('TC004 step 4: failed')

driver.quit()
