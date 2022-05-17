import requests                #引用requests物件
from bs4 import BeautifulSoup  #從bs4模組內引用BeautifulSoup物件
import time                    #引用time模組來計算程式所花費的時間用
import concurrent.futures      #引用平行處理的模組

def scrape(links):

    
        response = requests.get(links)
            
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
        
        print(title_list)      #將抓取到的標題列印出來驗證
        print(tag_list)        #將抓取到的子網頁資料列印出來驗證

start_time = time.time()
links = [ 
    f'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt/page/{page}' for page in range(1,4)]
    #執行多執行緒必須先建立網址清單
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:  #用with方法啟用多執行緒，max_worker是用來設定幾個執行緒的
    executor.map(scrape,links)    #將執行緒配置(map)給scape函式。因為函式有傳入連結網址的清單，所以要加links

end_time = time.time()
print(f'花費{end_time - start_time}秒')