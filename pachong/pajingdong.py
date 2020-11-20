from urllib import request
from urllib import parse
import urllib
import re
import ssl
import http.cookiejar
header1={
'Accept':'text/html',
'Accept-Language':'zh-CN,zh;q=0.8',
'content-type': 'text/html',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
'referer': 'https://item.jd.com/100010414404.html'
}

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

context = ssl._create_unverified_context()
page1=1
request.urlopen("https://jd.com",context=context)
while(page1<10):
    req = request.Request("https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&page="+str(page1)+"&click=0",headers=header1)
    page = request.urlopen(req,context=context).read().decode('utf-8')
    result = re.findall("<a target=\"_blank\" title=\".*?\" href=\"(.*?)\" onclick=",page)
    for u in result:
        page3=1
        id=re.findall("item.jd.com/(.*?).html",u)[0]
        req2 = request.Request("https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv134&productId="+id+"&score=0&sortType=5&page="+str(page3)+"&pageSize=10&isShadowSku=0&rid=0&fold=1",headers=header1)
        page2 = request.urlopen(req2,context=context).read().decode('gbk')
        result2 = re.findall("\"content\":\"(.*?)\",\"",page2)
        for i in result2:
            print(i)
    page1+=2