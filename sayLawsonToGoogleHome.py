# -*- coding: utf-8 -*-

import requests
import datetime
import locale
import sys
from time import sleep
from pytz import timezone
yobi = ["月","火","水","木","金","土","日"]

import urllib2
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
url = 'http://www.lawson.co.jp/ponta/tsukau/otameshi'

html = urllib2.urlopen(url)

soup = BeautifulSoup(html, "html.parser")

title_tag = soup.meta
url2 = soup.meta.get('content')
url = 'http://www.lawson.co.jp' + url2.split('=')[1]

html = urllib2.urlopen(url)
soup = BeautifulSoup(html, "html.parser")
title_tag = soup.title

#JST = timezone(timedelta(hours=+9), 'JST')
say_google_string = '今日のローソンのお試し引換券は、'
isFoundItem = 0
for section in soup.body.find_all('section'):
    #print section.get('id')
    if section.get('id') == 'sec-02':
        #print section
        for li in section.find_all('li'):
            #print '--------'
            #print li.find('p').unwrap()
            #print li
            #if li:
            #    continue
            #date = li.find('dl')
            #print date
            date = li.find('dd')
            if date == None:
                continue
            date_string = date.string.encode('utf_8')
            d = datetime.now()#.strftime("%Y.%m.%d")
            d = d + timedelta(hours=+9)
            today = d.strftime("%Y.%m.%d")
            #print date_string
            #print today
            if today == date_string:
                item_name = li.find('p')
                #print item_name
                if item_name == None:
                    continue
                #print item_name.string
                if len(say_google_string) + len(item_name.string.encode('utf_8')) > 256:
                    response = requests.post('http://192.168.1.49:8091/google-home-notifier', data={'text': say_google_string})
                    print(response.status_code)    # HTTPのステータスコード取得
                    print(response.text)           # レスポンスのHTMLを文字列で取得
                    say_google_string = ''
                    sleep(16)
                say_google_string = say_google_string + item_name.string.encode('utf_8') + ','
                isFoundItem = 1
            #print li.div.p.unwrap()
#print say_google_string
#v = [say_google_string[i: i+256] for i in range(0, len(say_google_string), 256)]
if isFoundItem == 0
    say_google_string = say_google_string + 'ありません'

if len(say_google_string) > 0:
    response = requests.post('http://192.168.1.49:8091/google-home-notifier', data={'text': say_google_string})
    print(response.status_code)    # HTTPのステータスコード取得
    print(response.text)           # レスポンスのHTMLを文字列で取得
