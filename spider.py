import requests
import csv
import json
from time import sleep
from lxml import html

# cookie 是需要替换的，referer 最好是替换一下
headers = {
    'sec-ch-ua': 'Google Chrome 77',
    'sec-fetch-mode': 'cors',
    'dnt': '1',
    'x-ig-www-claim': 'hmac.AR1P1exDcpFRvpFAYKNm_Wnajygy1QK5l3HC7cN5943dNlY-',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'sec-fetch-dest': 'empty',
    'x-requested-with': 'XMLHttpRequest',
    'cookie': r'ig_cb=2; ig_did=8C2C61E0-0456-45FF-9E99-31861120C1AA; mid=X_7vRAALAAHu0RobSwgjnWNt2Rpf; csrftoken=6vxLYu7FK0KOVA4WEFWAl9F6zIY3rpOA; ds_user_id=1435603015; sessionid=1435603015%3AJnfudDplPxwfac%3A3; shbid=19166; shbts=1610542919.267411; rur=NAO; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=GczGeVGzCky35Q4gZ_sxN8ICCGhKeo8cMIdG7GvC3H0.eyJ1c2VyX2lkIjoiMTAwMDA3NTg4MDY1MTQ1IiwiY29kZSI6IkFRQmRzRVNad2VwcDFQVjZfYlE3dWpBcjNodm4tTmdJQk1TM1dUMVRxRzZHR3VVMV9YRk5sUzNrT2cwXy0xVGFzQXN0WnlfU1FyejZTZ0dOdWpiSEFqWl8zVU9UUFg0Tmt5LTBHNHgtVHNzQVNGbDhSZ1VzZnlmQUtKM1N6eEkzWlVpUVJWN2V5UnptcEpQc3ZEbHpRRnhNYktvbzg3SkdUV0JjcmtjRlYtanBJbUZ4RTRKNVROa1NFbmUzRDFOU2RIZlJfdm5hNGp0LTBVTmFJV2ZwWXJMUUZWeDJaOE1KOVhxUTU1TVQtREJPcnk2N0xXUFdFdXk1bHBHYzd1ZFE4NXg3YkMyWWlvWjBhc0N6d2k0LUNPYWpHV3dYZGZxRmVkbVBJRVY2V29idnd4Rm1ITHkxOEdVZFNVN2hjajU0Q2xVQy1xV1luaXlJOEVkX0czUWh6cTBJIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU1PZUJQY0lXUEt2U2h1U1JLRmJLZWxPSVV3U2dSdW1nNDNUUEtNNWtXVFpBVjNaQ2Z2RE15SDZaQjlPMVZjRjBURkxNVkY5WkI2SWhaQWVJZWpqMGVJQlQzb2U3eTJjWWpBa2xNRkNtY20yWkFTMnZweHM1RGR2SXBXN1RaQU9JSU51V0g5VnR0UnZJWkJqbXNyNmd5V3J5akRUaFloTGc1eGZJb3Z2dzQ2SiIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjEwNTQzMzI3fQ; urlgen="{\"82.21.85.137\": 5089}:1kzfxQ:zhO48U9dECzzMSvjbUmK07N4kEk"',
    'x-csrftoken': '1vBpb3wLDDDbC63ckwu06IzIy351nB12',
    'x-ig-app-id': '936619743392459',
    'accept-encoding': 'gzip, deflate, br',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
    'accept': '*/*',
    'referer': 'https://www.instagram.com/linda_ledo_carlights/following/',
    'authority': 'www.instagram.com',
    'sec-fetch-site': 'same-origin',
}

end_cursor = ''
has_next = True

while has_next:
    # id是需要替换的，每一个用户的 id 不一样
    params = (
        ('query_hash', '3dec7e2c57367ef3da3d987d89f9dbc8'),
        ('variables',
         '{"id":"1203772139","include_reel":true,"fetch_mutual":false,"first":12,"after":"' + end_cursor + '"}'),
    )

    response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params).text

    res = json.loads(response)
    has_next = res['data']['user']['edge_follow']['page_info']['has_next_page']
    print(has_next)
    end_cursor = res['data']['user']['edge_follow']['page_info']['end_cursor']
    edges = res['data']['user']['edge_follow']['edges']

    out = open("ig.csv", "a+", newline="", encoding="utf-8-sig")
    csv_writer = csv.writer(out, dialect="excel")

    for i in edges:
        row = [i['node']['id'], i['node']['username'], i['node']['full_name']]
        csv_writer.writerow(row)

    out.close()
    sleep(23.3)

print("=============Done==============")