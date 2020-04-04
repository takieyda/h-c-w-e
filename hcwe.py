		○ #!/usr/bin/python3
		import requests
		from bs4 import BeautifulSoup
		from datetime import datetime
		from hashlib import md5
		
		url = ''
		port = 
		
		def getText(a):
		    body = list(list((BeautifulSoup(a.text, "html.parser")).children)[0].children)[3]
		    text = (list(body.children)[2]).get_text()
		    slow = (list(body.children)[3]).get_text()
		    return text, slow
		
		start = datetime.now()
		
		page = requests.get('http://{}:{}/'.format(url, port))
		#print('--- Text ---\n\n{}'.format(page.text))
		#print('--- Headers ---\n\n{}'.format(page.headers[))
		phpsessid = page.cookies['PHPSESSID']
		print('PHPSESSID:\t{}\n'.format(phpsessid))
		
		
		text = getText(page)[0]
		print('Text string:\t{}'.format(text))
		
		md5hash = md5(text.encode('utf-8')).hexdigest()
		print('MD5 hash:\t{}\n'.format(md5hash))
		
		params = {"hash": md5hash}
		headers = {"Content-type": "application/x-www-form-urlencoded"}
		cookies = {"PHPSESSID": phpsessid}
		post = requests.post('http://{}:{}/'.format(url, port),
		                     headers=headers, cookies=cookies, data = params)
		#print(post.text)
		
		print("Duration:\t{}\n".format(datetime.now() - start))
		
		print("Status:\t\t{} {}\n".format(post.status_code, post.reason))
		
		if getText(post)[1] == "Too slow!":
		    print("Result:\t\tToo slow!")
		else:
		    print(post.text)
