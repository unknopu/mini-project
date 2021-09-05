from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# from bs4 import BeautifulSoup as soup
import time
import os
import urllib.request
import wget
import random

path = r'/Users/50696e67/Downloads/Beautify github/chromedriver'
url = 'https://www.instagram.com/'
driver = webdriver.Chrome(path)
driver.get(url)

# Start login 
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username.clear()
username.send_keys("CENSOR")
password.clear()
password.send_keys("CENSOR")
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()


# Target the search field
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()
keyword = "SOMEONE'S IG"
searchbox.send_keys(keyword)
time.sleep(3)
searchbox.send_keys(Keys.ENTER)
searchbox.send_keys(Keys.ENTER)

time.sleep(3)
# driver.execute_script("window.scrollTo(0, 4000);")
imgs = driver.find_elements_by_tag_name('img')
imgs = [img.get_attribute('src') for img in imgs]
# for img in imgs:    
#     print('-------------\n' + str(img))


path = os.getcwd()
path = os.path.join(path, keyword[1:] + chr(random.randint(65, 90)))
os.mkdir(path)
# print('\n-----------------\n'+ str(path))

counter = 0
for img in imgs:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    
    print('\n-----------------\n'+ str(save_as))
    urllib.request.urlretrieve(img, save_as)
    counter += 1

driver.close()
