from bs4 import BeautifulSoup
import requests
from csv import writer


response = requests.get('http://sites url')
soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.find_all(class_='class you want to target')
with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headersv = ['Title', 'Link', 'Date']

for post in posts:
    print(post)
    #title = post.find(class_='post-title').get_text().replace('\n', '')
    # print(title)
