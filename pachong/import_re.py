Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import requests
>>> r=requests.get("http://python123.io/ws/demo.html")
>>> demo=r.text
>>> from bs4 import BeautifulSoup
>>> soup=BeautifulSoup(demo, 'html.parser')
>>> tag=soup.a
>>> for tag in soup.find_all(Ture):
	print(tag.name)

	
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    for tag in soup.find_all(Ture):
NameError: name 'Ture' is not defined
>>> for tag in soup.find_all(True):
	print(tag.name)

	
html
head
title
body
p
b
p
a
a
>>> import re
>>> for tag in soup.find_all(re.compile('b')):
	print(tag.name)

	
body
b
>>> soup.find_all('p','course')
[<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>]
>>> soup.find_all(id='link1')
[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>]
>>> soup.find_all(id-'link')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    soup.find_all(id-'link')
TypeError: unsupported operand type(s) for -: 'builtin_function_or_method' and 'str'
>>> soup.find_all(id='link')
[]
>>> import re
>>> soup.find_all(id=re.compile('link'))
[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]
>>> import re
>>> soup.find_all(string=re.compile("python"))
['This is a python demo page', 'The demo python introduces several python courses.']
>>> 
