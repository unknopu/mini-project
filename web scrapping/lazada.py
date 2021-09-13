from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import random

# Core driver
chrome_options = webdriver.ChromeOptions()
path = os.path.abspath('chromedriver')
url = r'https://sellercenter.lazada.co.th/apps/order/index?spm=a1zawg.17752401.navi_left_sidebar.droot_normal_ordersreviews_ordersnewui.16714edf8eiuTC'
driver = webdriver.Chrome(path, chrome_options=chrome_options)
driver.get(url)

# Start login 
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='TPL_username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='TPL_password']")))
username.clear()
username.send_keys("CENSOR")
password.clear()
password.send_keys("CENSOR")
button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='next-btn next-medium next-btn-normal btn aplus-auto-exp aplus-auto-clk']"))).click()
tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='next-tabs-tab-inner']"))).click()



