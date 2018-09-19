from bs4 import BeautifulSoup
from selenium import webdriver

# path to phantomjs executable
browser = webdriver.PhantomJS(
    '/home/tsokis/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

# url we want to target
url = 'https://www.nba.com/players'

# downloading the web page
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'lxml')

#section = soup.find('section', class_='block-league-content')
#section = soup.find('section', class_='row nba-player-index__row')
# getting all nba's players name
section = soup.find('section', class_='row expanded ')

for player in section.find_all('a'):
    print player.text
    #print player['href']


#print section

#print browser.page_source

browser.quit()
