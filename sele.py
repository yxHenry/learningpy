import requests
import os
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

def download(folder,url):
    if not os.path.exists(folder):
        os.makedirs(folder)
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        name = url.split('/')[-1]
        f = open("./"+folder+'/'+name,'wb')
        f.write(req.content)
        f.close()
        return True
    else:
        return False

driver = webdriver.Chrome()
driver.get("http://m.weibo.cn/")
assert "欢迎登录" in driver.title
elem = driver.find_element_by_xpath("/html/body/div/div/a[2]").click()
time.sleep(2)
driver.find_element_by_id("loginName").send_keys("yangxiang_1994@163.com")
driver.find_element_by_id("loginPassword").send_keys("989727yx")
driver.find_element_by_id("loginAction").click()
time.sleep(2)
driver.find_element_by_class_name('iconf_navbar_search').click()
time.sleep(2)
search = driver.find_element_by_name("queryVal")
search.send_keys("大爷来玩嘛")
search.send_keys(Keys.RETURN)
time.sleep(2)
enter = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div[2]/div/h3/span')
enter.click()
# elem.send_keys("刘亦菲")
# elem.send_keys(Keys.RETURN)
# print(driver.page_source)