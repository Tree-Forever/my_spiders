import json
import requests

avid = 615045557  #av号 = oid
page = '0'   #页数

url = 'https://api.bilibili.com/x/v2/reply/main'
params = {
       'oid': avid,
       'next': page,
       'type': '1',
}
response = requests.get(url, params=params)
data = response.json()['data']

# cusor = data['cursor'] #下一页的页数
repiles = data['replies'] #评论列表
# top_replies = data['top_replies'] #置顶评论列表
upper = data['upper']['mid'] #up主的id

for reply in repiles:
    rpid = reply['rpid'] #评论id
    mid = reply['mid'] #评论者id
    like = reply['like'] #点赞数
    rcount = reply['rcount'] #回复数
    ctime = reply['ctime'] #评论时间
    message = reply['content']['message'] #评论内容
    print(message)