import requests

oid = 1171011658 #av号 = oid
pid = 615045557

date = '2023-06-22'
Cookie = ""
url = "https://api.bilibili.com/x/v2/dm/web/seg.so"
params = {
    'oid': oid,
    'pid' : pid,
    'type': '1',
    'segment_index' : 1,
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Cookie': Cookie
}

response = requests.get(url, params=params, headers=headers)

def bytesToHexString(bs):
    return int.from_bytes(bs, byteorder='big', signed=True)

print(bytesToHexString(response.content[0:100]))
# print(response.text[0:1000])
# hú¶¤ÕÜ (ÿÿÿ2580d68c0:非洲斑猎犬祖传掏裆@ПѤHb1345183359302843648p̩´¢0ª0
'''
color: 16777215
date: 1687449552
dmid: "1345183359302843648"
mode: 1
size: 25
stime: 77379
text: "非洲斑猎犬祖传掏裆"
uhash: "580d68c0"
'''