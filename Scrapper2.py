import urllib.request
import urllib.parse
import re

url = 'http://feeds.bbci.co.uk/news/world/rss.xml'
#values = {'s':'basics','submit':'search'}
values = {}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

#print(respData)

result1 = re.findall(r'<description>(.*?)</description>',str(respData))  # every thing in paragraph tag

localsensors = "Local sensor's readings. Your current room temp "+'10'+" degrees celsius"

news = ""  
 
for eachr1 in result1:
    news = news +'\n' +eachr1
 
news = news + '\n' +localsensors 
 
print(news)	
	
	
