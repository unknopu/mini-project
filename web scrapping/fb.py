from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# from bs4 import BeautifulSoup as soup
import time
import os
import urllib.request
import random

# Core driver
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
path = r'/Users/50696e67/Downloads/Beautify github/chromedriver'
url = 'https://www.facebook.com/'
driver = webdriver.Chrome(path, chrome_options=chrome_options)
driver.get(url)

# Start login
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
username.clear()
username.send_keys("CENSOR")
password.clear()
password.send_keys("CENSOR")
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

imgs = []
for i in ['/set/?set=a.262425337119149']:
    driver.get('https://www.facebook.com/media/' + i)
    time.sleep(5)

    n_scrolls = 2
    for j in range(1, n_scrolls):
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(5)
        lst = ['https://scontent.fbkk22-1.fna.fbcdn.net/v/t1.0-9/',\
            'https://scontent.fbkk22-2.fna.fbcdn.net/v/t1.0-9/',\
                'https://scontent.fbkk22-3.fna.fbcdn.net/v/t1.0-9/']
        anchors = driver.find_elements_by_tag_name('img')
        anchors = [a.get_attribute('src') for a in anchors]
        anchors = [a for a in anchors if str(a).startswith(lst[0])]
        print('\n---------------------\n')
        print(anchors)

        # print('\n---------------------\n')
        # for a in anchors:
        #     driver.get(a)
        #     time.sleep(5)
        #     print(a)

        # for a in anchors:
        #     driver.get(a)
        #     time.sleep(5)
        #     img = driver.find_elements_by_tag_name('img')
        #     imgs.append(img[1].get_attribute('src'))
        #     for k in img:
        #         print(k.get_attribute('src'))
# print('\n\n\n', imgs)
