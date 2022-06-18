from bs4 import BeautifulSoup
import requests
import json
import time
import re
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
loginURL = 'http://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/bookmark.php'


def login(id, passwd):
    headers = {'User-Agent': userAgent}
    userData = {'version': '0', 'id': id, 'password': passwd, 'term': 'on', }
    res = requests.Session().post(loginURL, data=userData, headers=headers)
    res.encoding = 'uft-8'
    soup = BeautifulSoup(res.text, 'html5lib')
    if soup.find('meta', attrs={'http-equiv': 'expires'}):
        print(soup.title.string)
        print('登入失敗')
    else:
        metaTag = soup.find(
            'meta', attrs={'http-equiv': 'refresh'}).get('content')
        session_id = metaTag.split('session_id=')[1]
        print('登入成功！ 本次登入session:', session_id)
    return session_id


if __name__ == "__main__":
    with open('setting.json', encoding='utf-8') as f:
        data = json.load(f)
    id = data['stuID']
    passwd = data['password']
    session_id = login(id, passwd)
