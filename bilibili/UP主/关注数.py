import requests

uid='393396916' #贾布加布

url = 'https://api.bilibili.com/x/relation/stat?vmid='+uid+'&jsonp=jsonp'
params = {
    'vmid':uid,
}
response = requests.get(url,params=params)

data = response.json()['data']

following = data['following'] #关注数
follower = data['follower'] #粉丝数
print('关注数：',following)
print('粉丝数：',follower)
