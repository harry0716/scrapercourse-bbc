import requests                #引用requests物件
from bs4 import BeautifulSoup  #從bs4模組內引用BeautifulSoup物件


response = requests.get(
    'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt') #利用get函式抓取網頁

soup = BeautifulSoup(response.text,'lxml')  #利用BS套件的抓取網頁內的文字text，也利用lxml
titles = soup.find_all('span',{'class':'lx-stream-post__header-text gs-u-align-middle'}) #用find_all抓取網頁上所有的標題文字

title_list = []                          #建立一個title_list空串列，為了之後將抓取到的標題文字加入這個空串列
for title in titles:                     #運用for 迴圈將每次抓取的標題文字
    title_list.append(title.getText())   #運用append指令將抓取到的標題文字加入title_list串列中          
    
print(title_list)                        #印出title_list串列
