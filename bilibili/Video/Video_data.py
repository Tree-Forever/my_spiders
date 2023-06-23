import requests
import re
import json

bvid = 'BV1ah4y1u7YC'

url = 'https://www.bilibili.com/video/' + bvid
response = requests.get(url)
html = response.text

pattern = r"window\.__INITIAL_STATE__=(.*?);"
result = json.loads(re.findall(pattern, html)[0])

videoData = result['videoData']
bvid = videoData['bvid']
aid = videoData['aid']
cid = videoData['cid']

pic = videoData['pic'] # 封面
title = videoData['title'] # 标题
pubdate = videoData['pubdate'] # 发布时间
# ctime = videoData['ctime'] # 创建时间
desc = videoData['desc'] # 简介

owner = videoData['owner'] # up主信息 
mid = owner['mid'] # up主id
# name = owner['name'] # up主名字
# face = owner['face'] # up主头像

stat = videoData['stat'] # 观看等信息
view = stat['view'] # 播放量
danmaku = stat['danmaku'] # 弹幕数
reply = stat['reply'] # 评论数
favorite = stat['favorite'] # 收藏数
coin = stat['coin'] # 硬币数
share = stat['share'] # 分享数
now_rank = stat['now_rank'] # 当前全站日排行
his_rank = stat['his_rank'] # 历史最高全站日排行
like = stat['like'] # 点赞数
dislike = stat['dislike'] # 点踩数


dimension = videoData['dimension'] # 分辨率
width = dimension['width'] # 宽
height = dimension['height'] # 高

# pages = videoData['pages'] # 分p信息

try:
    honor_reply = videoData['honor_reply']['honor'] # 获得的荣誉
except:
    honor_reply = None

tags = result['tags']# 标签

for tag in tags:
    tag_id = tag['tag_id'] # 标签id
    tag_name = tag['tag_name'] # 标签名字
    tag_type = tag['tag_type'] # 标签类型
    
print(aid,bvid,cid)