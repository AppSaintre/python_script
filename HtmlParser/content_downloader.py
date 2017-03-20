import urllib.request as req
import urllib.error as ue
from bs4 import BeautifulSoup
import re
import os
import sys #a one-time usage

cpath = './download/'
urlhp = 'http://esl-lab.com/'
urlmp3 = 'http://esl-lab.com/audio/mp3/'

def dlfromFile(file,mode=0): #mode 0: download doc only; 1: doc and mp3
	fh = open(file,'r')
	repl = ['rd1','sc1']
	for line in fh:
		parse = re.findall('(\S+)/',line)
		name = parse[0]
		path = cpath + name
		filename = path + '/' + name + '.mp3'
		srcurl = urlmp3 + name + '.mp3'
		if mode==1:
			try:
				srcpg = req.urlopen(srcurl)
				if(srcpg.getcode()==200):
					fhand = open(filename,'wb')
					for dline in srcpg:
						fhand.write(dline)
					fhand.close()
					srcpg.close()
					print('MP3 OK:',line)
			except ue.HTTPError as e:
				print('MP3 ',e.code,':',line)
		ctntdl(line,name)
	fh.close()
		
def ctntdl(url,name):
	path = cpath + name
	repl = ['rd1','sc1']
	filename = path + '/' + name + '.html'
	srcurl = urlhp + url.replace(repl[0],repl[1])
	try:
		srcpg = req.urlopen(srcurl)
		if(srcpg.getcode()==200):
			fhand = open(filename,'w')
			for line in srcpg:
				fhand.write(line.decode('utf-8','ignore')) 
				#ignore chars which can not be interpreted by utf-8
			fhand.close()
			srcpg.close()
	except ue.HTTPError as e:
		print('DOC ',e.code,':',url)
	
def mp3dl(url,name):
	path = cpath + name
	filename = path + '/' + name + '.mp3'
	srcurl = urlmp3 + name + '.mp3'
	if not os.path.exists(path):
		os.makedirs(path)
	try:
		srcpg = req.urlopen(srcurl)
		if(srcpg.getcode()==200):
			fhand = open(filename,'wb') #Write Bytes
			for line in srcpg:
				fhand.write(line)
			fhand.close() #explicitly close
			srcpg.close() #explicitly close
			print('MP3 OK:',url)
	except ue.HTTPError as e:
		print('MP3 ',e.code,':',url)
	ctntdl(url,name)
	
#dlfromFile("remn.txt")
#sys.exit()
hp = req.urlopen(urlhp)
urlfile = 'urls.txt'
furls = open(urlfile,'w')
marks = ['<BR><A HREF=']
for line in hp:
	linestr = line.decode('utf-8')
	if marks[0] in linestr:
		res = re.findall('<BR><A HREF=\"(\S+)\"',linestr)
		#name = re.findall('(\S+)/',res[0]) 
		#mp3dl(res[0],name[0])] #maybe too long time for a connection
		furls.write(res[0]+'\n')
furls.close()
hp.close()
#dlfromFile(urlfile,1)
		
		
		
		
		