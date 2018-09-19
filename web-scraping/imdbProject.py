from bs4 import BeautifulSoup
from selenium import webdriver

# path to phantomjs executable
browser = webdriver.PhantomJS(
    '/home/tsokis/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

# imdb Top Rated Movies url
url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'

# downloading the web page
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'lxml')
# targeting the table tag with className = chart
table = soup.find('table', class_='chart')


for movie in table.find_all('td', class_='titleColumn'):
    # ----with print movie.text we get our info but in an ugly shape
    #print movie.text
    # ----formatting the text so it can look better on terminal
    info = movie.text.strip().replace('\n', '').replace('      ', '')
    print info
    ranks = info.split('.')[0]
    print 'Rank of the movie: ' + ranks
    title = info.split('.')[1].split('(')[0]
    print 'Title of the movie: ' + title
    year = info.split('(')[1][:-1]
    print 'Year: ' + year + '\n'


browser.quit()
