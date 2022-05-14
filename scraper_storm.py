import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.storm.mg/category/249515')

soup = BeautifulSoup(response.text,'lxml')
titles = soup.find_all('span',{'class':'link_text'},)
titles_1 = soup.find_all('h2',{'class':'card_title'})
titles_2 = soup.find_all('h3',{'class':'card_title'})

for title in titles:
    print(title.getText())

for title1 in titles_1:
    print(title1.getText())

for title2 in titles_2:
    print(title2.getText())


