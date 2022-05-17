import requests
from bs4 import BeautifulSoup

response = requests.get(
    'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt')

soup = BeautifulSoup(response.text,'lxml')
titles = soup.find_all(
    'span',{'class':'lx-stream-post__header-text gs-u-align-middle'})

title_list = []
for title in titles:
    title_list.append(title.getText())

urls = soup.find_all(
    'a',{'class':'qa-heading-link lx-stream-post__header-link'})

tag_list = []
for url in urls:
    sub_response =  requests.get('https://www.bbc.com' + url.get('href'))
    sub_soup = BeautifulSoup(sub_response.text, 'lxml')
    tags = sub_soup.find_all('li',{'class':'bbc-1msyfg1 e1hq59l0'})
    for tag in tags:
        tag_list.append(tag.getText())
        # tag.find('a').getText()   # 因為a標籤包含在li標籤下，所以也可以將find('a')省略，此處是完整寫法
print(tag_list)