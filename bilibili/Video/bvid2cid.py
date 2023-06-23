import requests

bvid = 'BV1Ph411C7S5'

url = "https://api.bilibili.com/x/player/pagelist"
params = {
    'bvid' : bvid,
}
response = requests.get(url, params=params,timeout=10)

# print(response.text)
#{"code":0,"message":"0","ttl":1,"data":[{"cid":293298061,"page":1,"from":"vupload","part":"夜に駆けるMV","duration":276,"vid":"","weblink":"","dimension":{"width":1920,"height":1080,"rotate":0}}]}

cid = response.json()['data'][0]['cid']
print(cid)
