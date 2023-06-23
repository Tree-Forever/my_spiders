import requests
import time
uid = '393396916'  #关注的up主的uid
cookie = ""
url = 'https://api.bilibili.com/x/space/acc/relation'
params = {
    'mid':uid
}
headers = {
    'Cookie':cookie,
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36",
}

response = requests.get(url,params=params,headers=headers)
data = response.json()['data']['relation']

mtime = data['mtime']   # 关注时间
mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mtime))   # 将时间戳转换为时间字符串
special = data['special']   # 特别关注
print('关注时间：',mtime)
print('是特别关注?：',special)