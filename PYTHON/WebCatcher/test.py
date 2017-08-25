#coding:utf-8
__author__ = 'hang'

import warnings
warnings.filterwarnings("ignore")
import urllib2

from bs4 import BeautifulSoup as bs

#分析网页函数
def getNowPlayingMovie_list():
    resp = urllib2.urlopen('https://movie.douban.com/nowplaying/hangzhou/')
    html_data = resp.read().decode('utf-8')
    soup = bs(html_data, 'html.parser')
    nowplaying_movie = soup.find_all('div', id='nowplaying')
    nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')
    nowplaying_list = []
    for item in nowplaying_movie_list:
        nowplaying_dict = {}
        nowplaying_dict['id'] = item['data-subject']
        for tag_img_item in item.find_all('img'):
            nowplaying_dict['name'] = tag_img_item['alt']
            nowplaying_list.append(nowplaying_dict)
    return nowplaying_list


response = urllib2.urlopen("https://movie.douban.com/nowplaying/hangzhou/")
html_data = response.read().decode('utf-8')
print html_data
