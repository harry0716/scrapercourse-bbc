import requests                #引用requests物件
from bs4 import BeautifulSoup  #從bs4模組內引用BeautifulSoup物件

"""第5行至第15行，爬取BBC新聞網站的第一層網頁資料方法"""
response = requests.get(
    'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt') #利用get函式抓取網頁

soup = BeautifulSoup(response.text,'lxml')  #利用BS套件的抓取網頁內的文字text，也利用lxml
titles = soup.find_all('span',{'class':'lx-stream-post__header-text gs-u-align-middle'}) #用find_all抓取網頁上所有的標題文字

title_list = []                          #建立一個title_list空串列，為了之後將抓取到的標題文字加入這個空串列
for title in titles:                     #運用for 迴圈將每次抓取的標題文字
    title_list.append(title.getText())   #運用append指令將抓取到的標題文字加入title_list串列中          
    
"""爬取BBC新聞網站的子網頁資料方法"""

urls = soup.find_all('a',{'class':'qa-heading-link lx-stream-post__header-link'}) #用BS的soup方法找出所有對應的a標籤 
tag_list = []
for url in urls:
    sub_response = requests.get('http://www.bbc.com' + url.get('href'))
    sub_soup = BeautifulSoup(sub_response.text,'lxml')
    tags = sub_soup.find_all('li',{'class':'bbc-1msyfg1 e1hq59l0'})
    for tag in tags:
        tag_list.append(tag.getText())  #運用append指令將抓取到的標題文字加入tag_list串列中  
       # print(tag.find('a').getText()) #因為li下面只有一個a標籤，所以程式碼是可以省略.find('a')
    print(tag_list)
    

