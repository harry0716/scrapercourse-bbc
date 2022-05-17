import grequests                #引用grequests物件
from bs4 import BeautifulSoup  #從bs4模組內引用BeautifulSoup物件
import time                    #引用time模組，為了記錄程式執行時間

start_time = time.time()

links = [
    f'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt/page/{page}' for page in range(1,4)]

reqs =  (grequests.get(link) for link in links)      #用grequests.get將抓取到的links依據傳到變數reqs
resps = grequests.imap(reqs, grequests.Pool(3))      #用grequests.imap將reqs對應到grequests的對應池中pool(3)因為有三個links 
for index, resp in enumerate(resps):    #此處改用enumerate()及index，為了第37行

    soup = BeautifulSoup(resp.text,'lxml')  #利用BS對抓取的text進行解析
    titles = soup.find_all('span',{'class':'lx-stream-post__header-text gs-u-align-middle'}) #用find_all抓取網頁上所有的標題文字

    title_list = []                          #建立一個title_list空串列，為了之後將抓取到的標題文字加入這個空串列
    for title in titles:                     #運用for 迴圈將每次抓取的標題文字
        title_list.append(title.getText())   #運用append指令將抓取到的標題文字加入title_list串列中          
        
    """爬取BBC新聞網站的子網頁資料方法"""

    urls = soup.find_all(
        'a',{'class':'qa-heading-link lx-stream-post__header-link'}) #用BS的soup方法找出所有對應的a標籤 
    sub_links = ['http://www.bbc.com' + url.get('href') for url in urls]

    sub_reqs = (grequests.get(sub_link) for sub_link in sub_links)    #用grequests.get將抓取到的sub_links依據傳到變數sub_reqs
    sub_resps = grequests.imap(sub_reqs, grequests.Pool(10))          #用grequests.imap將reqs對應到grequests的對應池中

    tag_list = []
    for sub_resp in sub_resps:
        sub_soup = BeautifulSoup(sub_resp.text,'lxml')
        tags = sub_soup.find_all('li',{'class':'bbc-1msyfg1 e1hq59l0'})
        for tag in tags:
            tag_list.append(tag.getText())  #運用append指令將抓取到的標題文字加入tag_list串列中  
        # print(tag.find('a').getText()) #因為li下面只有一個a標籤，所以程式碼是可以省略.find('a')
    print(f'第{index+1}頁')   #參照第12行，for迴圈的索引值從0開始計算
    print(title_list)      #將抓取到的標題列印出來驗證
    print(tag_list)        #將抓取到的子網頁資料列印出來驗證
    
end_time = time.time()
print(f"花費{end_time - start_time}秒")
