from email import header
from wsgiref import headers
import requests                #引用requests物件
from bs4 import BeautifulSoup  #從bs4模組內引用BeautifulSoup物件

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}   #第一點，設定瀏覽器的標頭，而user-agent的值，可以在chrome瀏覽器搜雲"my user agent"就會有結果

#第五點要有例外處理機制可以用try,except
try:
    response = requests.get(
        'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt',headers=headers,timeout= 5) 
        #對瀏覽器發送requests請求，在超連結後面加上headers=headers(自己設定的)就OK了
        #第二點，timeout是設定請求的超時屬性，可以自訂秒數，預設單位是秒

    if response.status_code == 200:  #第三點，針對response的狀態回應碼200的檢查

        soup = BeautifulSoup(response.text,'lxml')  #利用BS套件的抓取網頁內的文字text，也利用lxml
        title = soup.find_all('span',{'class':'lx-stream-post__header-text gs-u-align-middle'}) #用find_all抓取網頁上所有的標題文字

        if title: #針對title(第4點元素是否存在)的檢查
            result = title.getText()
            print(result)
        else:
            print("元素不存在!")
    else:
        print('狀態碼非200!')

except Exception as e:
    print(str(e))
