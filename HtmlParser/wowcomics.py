import urllib.request as req

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  #Disguise



downlist = []
x = 0
offset = 12
while(x<14):
	downlist.append(x+offset)
	x = x + 1
pagelist = [23,24,23,22,23,24,22,27,23,24,23,23,35,39]	

def downcomic(loopnum,dir,svcurl):
	while(loopnum):
		fhand = open(dir+str(loopnum)+'.jpg','wb')
		props = req.Request(url=svcurl+str(loopnum)+'.jpg', headers=headers)  
		html = req.urlopen(props)
		for line in html:
			fhand.write(line)
		html.close()
		fhand.close()
		loopnum = loopnum - 1	

for li in downlist:
	lpn = pagelist[int(li)-offset]
	dr = 'comics/'+str(li)+'/'
	surl = 'http://www.readcomics.tv/images/manga/world-of-warcraft/' +str(li) + '/'
	downcomic(lpn,dr,surl)
	print(surl+'completed')

	