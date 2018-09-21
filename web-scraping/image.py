'''                     Download the image poster
---Chrome or Mozilla dev tools would be a good choice--
  Inspect the poster and you will find a <div> with the class of "poster",
  inside and below of that <div> is an href with this format  "/title/something/something/something?ref_=something",
  If you grab that href and paste it on your browser (ex: www.imdb.com/title/something/something/something?ref_=something), it will redirect you on the image poster
  If you inspect that image you will find, a -src- attribute,(ex: src"http://something") which is inside a <div> with the class of "pswp__zoom-wrap",
  So we want to target this div with the class"pswp__zoom-wrap" which has an image tag with some source attribute

Steps: 1) <div> with the class of "poster" 
       2) a['href']
       3) redirect: 'https://www.imdb.com' + a['href']
       4) <div> with class ="pswp__zoom-wrap"  
       5) image src attribute 

'''
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

url = 'https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=PJ932K9XJKQC6X2RXMAJ&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1'

browser = webdriver.PhantomJS(
    '/home/tsokis/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

browser.get(url)

soup = BeautifulSoup(browser.page_source, 'lxml')

div = soup.find('div', class_='poster')

# a tag
a = div.find('a')

print 'https://www.imdb.com' + a['href']

url = 'https://www.imdb.com' + a['href']

browser.get(url)

soup = BeautifulSoup(browser.page_source, 'lxml')

all_div = soup.find_all('div', class_='pswp__zoom-wrap')

all_img = all_div[1].find_all('img')
print all_img[1]['src']

# wb:write and binary check this link for further info https://stackoverflow.com/questions/2665866/what-is-the-wb-mean-in-this-code-using-python
file = open('poster_one.jpg', 'wb')
file.write(requests.get(all_img[1]['src']).content)
file.close()
browser.quit()
