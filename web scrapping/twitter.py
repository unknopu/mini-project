from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time

path = r'/Users/50696e67/Downloads/Beautify github/chromedriver'
opt = webdriver.ChromeOptions()
# background process option
opt.add_argument('headless')
driver = webdriver.Chrome(path, options=opt)

def twitter_post(twitter_name):
    print("\nRUNING {} ...\n".format(twitter_name))
    url = 'https://twitter.com/{}'.format(twitter_name)
    driver.get(url)

    time.sleep(5)
    # Scrolling page to x
    # pixel = 0
    # for i in range(0):
    #     driver.execute_script("window.scrollTo(9, {})".format(pixel))
    #     time.sleep(3)
    #     pixel += 10000
        
    page_html = driver.page_source

    # file = open('text.html', 'w')
    # file.write(page_html)
    # file.close()

    # paser the data from page
    data = soup(page_html, 'html.parser')
    posts = data.find_all('span', {'class': 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})

    # Clean data from post
    allpost = []
    mark = False
    for p in posts:
        txt = p.text
        if mark:
            allpost.append(txt)
            mark = False
        if txt == '·':
            mark = True
    return allpost


check_lst = ['elonmusk', 'BillGates', 'SpaceX']
for row in check_lst:
    posts = twitter_post(row)
    print('----------{}----------'.format(row))
    for post in posts:
        print(post)
        print("===================")

driver.close()