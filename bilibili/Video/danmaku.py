import requests

oid = 615045557 #av号 = oid
date = '2023-06-22'
Cookie = ""

url = "https://api.bilibili.com/x/v2/dm/web/history/seg.so"
params = {
    'oid': oid,
    'date': date,
    'type': '1',
}
headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
  'Cookie': Cookie
}

response = requests.get(url, params=params, headers=headers)

with open('danmaku.xml', 'wb') as f:
    f.write(response.content)
print(response.text)

