#!/usr/bin/python
from bs4 import BeautifulSoup
from datetime import datetime
from urllib import urlopen, urlencode
from httplib import HTTPConnection
from hashlib import md5

url = ""
port = ""

def getText(a):
    body = list(list((BeautifulSoup(a.read(), "html.parser")).children)[0].children)[3]
    text = (list(body.children)[2]).get_text()
    slow = (list(body.children)[3]).get_text()
    return text, slow

start = datetime.now()

page = urlopen("http://{}:{}/".format(url, port))

text = getText(page)[0]
print("Text string:\t{}".format(text))

md5hash = md5(text).hexdigest()
print("MD5 hash:\t{}\n".format(md5hash))

params = urlencode({"hash": md5hash})
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = (HTTPConnection(url, port))
conn.request("POST", "", params, headers)
response = conn.getresponse()

print("Duration:\t{}\n".format(datetime.now() - start))

print("Status:\t\t{} {}\n".format(response.status, response.reason))

if getText(response)[1] == "Too slow!":
    print("Result:\t\tToo slow!")
else:
    print(response.prettify())
conn.close()
