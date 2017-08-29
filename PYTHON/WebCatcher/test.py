#coding:utf-8
__author__ = 'yang'

import warnings
warnings.filterwarnings("ignore")
import urllib2
from bs4 import BeautifulSoup as bs


#分析网页函数
def getNowPlayingMovie_list():
    resp = urllib2.urlopen("https://movie.douban.com/nowplaying/hangzhou/")
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
            #print nowplaying_dict['name']
            nowplaying_list.append(nowplaying_dict)
            #print nowplaying_dict
    return nowplaying_list

#爬取评论函数
def getCommentsById(movieId, pageNum):
    eachCommentList = [];
    commentsString=''
    if pageNum>0:
         start = (pageNum-1) * 20
    else:
        return False
    requrl = 'https://movie.douban.com/subject/' + movieId + '/comments' +'?' +'start=' + str(start) + '&limit=20'
    print(requrl)
    resp = urllib2.urlopen(requrl)
    html_data = resp.read().decode('utf-8')
    soup = bs(html_data, 'html.parser')
    comment_div_lits = soup.find_all('div', class_='comment')
    for item in comment_div_lits:
        if item.find_all('p')[0].string is not None:
            eachCommentList.append(item.find_all('p')[0].string)
    return eachCommentList


def main():
    #循环获取第一个电影的前10页评论
    commentList = []
    NowPlayingMovie_list = getNowPlayingMovie_list()
    for i in range(1):
        num = i + 1
        commentList_temp = getCommentsById(NowPlayingMovie_list[0]['id'], num)
        commentList.append(commentList_temp)
    #print commentList




main()
