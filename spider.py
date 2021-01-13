import requests
from lxml import html
url='https://www.instagram.com/zjy5488142/' #Target website
page=requests.Session().get(url) 
tree=html.fromstring(page.text)
#result=tree.xpath('//td[@class="title"]//a/text()') #Accquire data