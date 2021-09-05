from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import os

# Core driver
chrome_options = webdriver.ChromeOptions()
# background process option
chrome_options.add_argument('headless')
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
path = r'/Users/50696e67/Downloads/Beautify github/chromedriver'
url = 'https://www.imdb.com/chart/top?sort=us,desc&mode=simple&page=1'
driver = webdriver.Chrome(path, chrome_options=chrome_options)
driver.get(url)

mname = driver.find_elements_by_class_name('titleColumn')
mname = [name.text for name in mname]

ratings = driver.find_elements_by_class_name('ratingColumn.imdbRating')
ratings = [r.text for r in ratings]

DF = pd.DataFrame({'MovieNames':mname , 'Ratings':ratings})

links = driver.find_elements_by_xpath("//td[@class='titleColumn']/a")
links = [link.get_attribute('href') for link in links]
DF['links'] = links

director = []
actor = []
character = []
story = []
genr = []
rd = []
wwg2 = []
rt =[]

for link in range(0, 250):
    #Open first links
    driver.get(links[link])
    #Get Director
    directors = driver.find_element_by_xpath("//div[@class='credit_summary_item']/a").text
    print('\n============== ' + str(link) + ' ' +str(director))

    #Get casts (ActorNames,CharactorNames)
    casts = driver.find_elements_by_xpath("//table[@class='cast_list']/tbody/tr")
    actors = [cast.text.split('...')[0] for cast in casts if str(cast.text.find('...')).isnumeric()]
    characters = [cast.text.split('...')[1] for cast in casts if str(cast.text.find('...')).isnumeric()]
    print('============== ' + str(link) + ' ' + str(actors) + str(characters))

    #Get storyline
    storys = driver.find_element_by_xpath("//div[@class='inline canwrap']/p/span").text
    genres = driver.find_elements_by_xpath("//div[@id='titleStoryLine']/div[@class='see-more inline canwrap']")[1].text
    genres = genres[genres.find(':')+2:]
    print('============== ' + str(link) + ' ' + str(storys) + str(genres))
    detail = driver.find_element_by_id("titleDetails").text

    #Get releasedate
    rdate = detail[detail.find('Release Date:')+14:]
    rdate = rdate[0:rdate.find('See more')-1]
    print('============== ' + str(link) + ' ' + str(rdate))

    #Get worldwidegross
    wwg = detail[detail.find('Cumulative Worldwide Gross:')+28:]
    wwg = wwg[0:wwg.find('See more')-1]
    print('============== ' + str(link) + ' ' + str(wwg))

    #Get runtime
    runtime = detail[detail.find('Runtime:')+9:]
    runtime = runtime[0:runtime.find('Sound')-1]
    print('============== ' + str(link) + ' ' + str(runtime))

    director.append(directors)
    actor.append(actors)
    character.append(characters)
    story.append(storys)
    genr.append(genres)
    rd.append(rdate)
    wwg2.append(wwg)
    rt.append(runtime)

DF['Director'] = director
DF['ActorNames'] = actor
DF['CharacterNames'] = character
DF['Storyline'] = story
DF['Runtime'] = rt
DF['Genres'] = genr
DF['Releasedate'] = rd
DF['Worldwidegross'] = wwg2


DF.to_csv('DF_Data.csv')


driver.close()