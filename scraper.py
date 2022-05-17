import requests                #引用requests物件
from bs4 import BeautifulSoup  #從bs4模組內引用BeautifulSoup物件

for page in range(1,4):    #增加for迴圈，以range方法確定要抓取的page的頁數

    """第5行至第15行，爬取BBC新聞網站的第一層網頁資料方法"""
    response = requests.get(
        f'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt/page/{page}') 
        #利用get函式抓取網頁，在請求網址的最後，加上page參數。
        #用f-string方法將for 迴圈中的page變數導入網址列的最後。

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
    print(f'第{page}頁')   #用f-string列印頁數
    print(title_list)      #將抓取到的標題列印出來驗證
    print(tag_list)        #將抓取到的子網頁資料列印出來驗證
    

