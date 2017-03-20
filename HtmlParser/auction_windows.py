import urllib.request as req
import urllib.parse as par
from bs4 import BeautifulSoup as bsoup
import sys

serviceUrl = 'http://auctions.search.yahoo.co.jp/search?'
keyword = input('Input Keywords(Devided by a Space):')
page = input('Which Page of the Result Do You Want:')
page = str((int(page)-1)*20 + 1)
pairs = {'p':keyword,'b':page}
url = serviceUrl + par.urlencode(pairs)
#print(url)
html = req.urlopen(url)
print(html)
#sys.exit()
start = 0
data = ''
for line in html:
	lineStr = line.decode('utf-8')
	if(start==0):
		if '<!-- SET01 -->' in lineStr:
			start = 1
	else:
		data = data + lineStr
tagList = bsoup(data,'html.parser')
aTags = tagList('a')
dedup = 0
for tag in aTags:
	resUrl = tag.get('href',None)
	if '/jp/auction/' in resUrl and dedup%2==0:
		probe = 0
		html = req.urlopen(resUrl)
		marks = ["評価制限","あり","なし"]
		for line in html:
			lineStr = line.decode('utf-8')
			if marks[0] in lineStr:
				probe = 1
			if marks[1] in lineStr and probe==1:
				break
			if marks[2] in lineStr and probe==1:
				print('A Satisfying Res:',resUrl)
				break
	dedup = dedup + 1
	

  
