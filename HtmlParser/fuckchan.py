#Download all your essays in renren
#Step:
#1. Log in within browser which eliminates bar code authentication
#2. Run this script, but first modify it by replacing <Your Email> and <Your Password> with your id and psw
#   such as 12345@fuckchan.com and 12345fuckchanecho
import requests
import sys,os
import codecs
import re

def myprint(s):
    sys.stdout.buffer.write(s.encode('utf-8', errors='replace'))

def essayDl(eurl,uid,sess):
	isLast = False
	dlpath = 'fuckchan/'
	eid = re.findall(uid +'/([0-9]+)',eurl)[0]
	while not isLast:
		nfile = dlpath + 'essay_' + eid + '.html'
		ec = sess.get(eurl)
		fhand = codecs.open(nfile,'w','utf-8')
		fhand.write(ec.text)
		fhand.close()
		print('Finish downloading essay_',eid)
		res = re.findall('旧一篇',ec.text)
		if len(res) == 0:
			isLast = True
		else:
			eurl = re.findall('(http://blog.renren.com/blog/'+ uid +'/[0-9]+)',ec.text)[-2]
			eid = re.findall(uid +'/([0-9]+)',eurl)[0]

def main():
	dlpath = 'fuckchan/'
	if not os.path.exists(dlpath):
		os.mkdir(dlpath)
	payload = {
		'email': '<Your Email>',
		'password': '<Your Password>'
	}
	with requests.Session() as s:
		p = s.post('http://www.renren.com/PLogin.do', data=payload)
	pat = 'http://www.renren.com/([0-9]+)/profile'
	uid = re.findall(pat,p.text)[0]
	blog_url = 'http://blog.renren.com/blog/' + uid + '/myBlogs'
	p = s.get(blog_url)
	furl = re.findall('(http://blog.renren.com/blog/'+ uid +'/[0-9]+)',p.text)[0]
	essayDl(furl,uid,s)

if __name__ == '__main__':
	main()
