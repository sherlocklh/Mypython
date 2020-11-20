import requests
import os
url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1537201752405&di=219e8e7db1aae1e83543fec9ea38d994&imgtype=0&src=http%3A%2F%2Fdingyue.nosdn.127.net%2FIv4t8xAwe3sp267QdQDIhmXxMognIdzryVx7cq5u8REhD1525931032055.jpg"
root = "D://pics//"
path = root+url.split('%2F')[-1]
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r=requests.get(url)
		with open(path,'wb') as f:
			f.write(r.content)
			f.close()
			print("文件保存成功")
	else:
		print("文件已存在")
except:
	print("爬取失败")