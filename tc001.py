# Automated system testing of an e-commerce store 'Magento'.

# Test case 1 (TC001) - homepage and Mobile menu.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Preconditions - the website http://live.techpanda.org/index.php/ is open.

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://live.techpanda.org/index.php/')

# Test step 1 - verify title of the page.
# Expected result - text 'THIS IS DEMO SITE' is displayed in the homepage.

expected_text = 'THIS IS DEMO SITE'
actual_text = driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]').text
try:
    assert actual_text.startswith(expected_text)
    print('TC001 step 1: passed')
except AssertionError:
    print('TC001 step 1: failed')
    print(actual_text)

# Test step 2 - open the Mobile menu.
# Expected result - the Mobile menu is open.

driver.find_element(By.XPATH, '//*[@id="nav"]/ol/li[1]/a').click()
expected_url = 'http://live.techpanda.org/index.php/mobile.html'
actual_url = driver.current_url
try:
    assert actual_url == expected_url
    print('TC001 step 2: passed')
except AssertionError:
    print('TC001 step 2: failed')
    print(actual_url)

# Test step 3 - verify the title of the page.
# Expected result - the title 'MOBILE' is displayed in the menu.

expected_title = 'MOBILE'
actual_title = driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div[2]/div[1]/div[1]').text
try:
    assert actual_title == expected_title
    print('TC001 step 3: passed')
except AssertionError:
    print('TC001 step 3: failed')
    print(actual_title)

# Test step 4 - sort the products by name.
# Expected result - all 3 products are sorted by name.

select = Select(driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div[2]/div[1]/'
                                              'div[3]/div[1]/div[1]/div/select'))
select.select_by_visible_text('Name')
driver.implicitly_wait(3)
driver.get_screenshot_as_file('TC001.png')

driver.close()
