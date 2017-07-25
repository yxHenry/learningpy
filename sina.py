import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get('https://passport.weibo.cn/signin/login')
WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.ID,'loginName')))
time.sleep(1)

name_field = driver.find_element_by_id('loginName')
name_field.clear()
name_field.send_keys('yangxiang_1994@163.com')
password_field = driver.find_element_by_id("loginPassword")
password_field.clear()
password_field.send_keys('989727yx')
submit_button = driver.find_element_by_id('loginAction')
submit_button.click()
search_button = driver.find_element_by_class_name('fr iconf iconf_navbar_search')
search_button.click()
print(driver.get_cookies())
