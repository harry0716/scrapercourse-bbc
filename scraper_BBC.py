import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt")

soup = BeautifulSoup(response.text,'lxml')
titles = soup.find_all('span',{'class':'lx-stream-post__header-text gs-u-align-middle'})

for title in titles:
    print(title.getText())