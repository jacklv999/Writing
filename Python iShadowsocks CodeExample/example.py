# -*- coding:utf-8 -*-
import requests
import re
import json
from bs4 import BeautifulSoup
from prettytable import PrettyTable

hearders = {'Host': 'c.ishadowx.net',
'Connection': 'keep-alive',
'Cache-Control':'max-age=0',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3095.5 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.8',
'Cookie': '_gat=1; _ga=GA1.2.1648183599.1547599218; _gid=GA1.2.1222817685.1547599218',
'If-None-Match': '"6550-57f86860071b6-gzip"',
'If-Modified-Since': 'Tue, 15 Jan 2019 22:17:14 GMT'}


url = 'https://c.ishadowx.net/'

r = requests.get(url,headers=hearders)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, "html.parser")
'''pw = soup.find_all("h4",text=re.compile('Password'))
server = soup.find_all("h4",text=re.compile('IP Address'))
port = soup.find_all("h4",text=re.compile('Port'))'''

pw = soup.find_all('Password')
server = soup.find_all('IP Address')
port = soup.find_all('Port')



print (soup)
print (pw,server,port)


'''def f(s):
    return s.split(':')[1]


pw = list(map(f, [pw[0], pw[2], pw[4]]))
server = list(map(f, [server[0], server[1], server[2]]))
port = list(map(f, [port[0], port[1], port[2]]))
l = []
for i in range(3):
    d = {"method": "aes-256-cfb", "server": server[i], "password": pw[i], "remarks": "", "server_port": port[i]}
    l.append(d)

info = PrettyTable(["服务器", "端口", "密码"])
for i in range(3):
    info.add_row([server[i], port[i], pw[i]])
print(info)


def get_pw(j):
    for x in range(len(j)):
        yield j[x]["server"], j[x]["password"]


with open("config.json", "r") as c:
    p = json.load(c)
    p = p["gui-config-path"]
    with open(p, "r") as s:
        j = json.load(s)
        j["configs"] = l
        with open(p, "w") as n_c:
            try:
                json.dump(j, n_c)
                print("写入成功")
            except:
                print("写入失败")'''
