import requests
url="https://www.jd.com"
try:
	kv={'user-agent':'Mozilla/5.0'}
	r=requests.get(url,headers=kv)
	r.raise_for_ststus()
	r.encoding=r.apparent_encoding
	print(r.text[1000:2000])
except:
	print("爬取失败")