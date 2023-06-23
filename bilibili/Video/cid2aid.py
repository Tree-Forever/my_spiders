import requests

cid = 293298061

url = "https://hd.biliplus.com/api/cidinfo"
params = {
    'cid' : cid,
}
response = requests.get(url, params=params,timeout=10)

# print(response.text)
#{"code":0,"data":{"cid":293298061,"aid":204006965,"page":1,"title":"YOASOBI \u591c\u306b\u99c6\u3051\u308b (Yoru ni Kakeru) Official Music Video","subtitle":"\u591c\u306b\u99c6\u3051\u308bMV","mid":400813602,"author":"Ayase-YOASOBI","cover":"\/bfs\/archive\/eb8f6e419769caabebbdf4698c5cfffcdfe74e78.jpg","type":"vupload","vid":"","duration":276}}

aid = response.json()['data']['aid']
print(aid)
