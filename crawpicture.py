import requests
import json

# 爬取猫咪图片
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
requrl = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%8C%AB%E5%92%AA%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E7%8C%AB%E5%92%AA%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&force=&pn=30&rn=30&gsm=1e&1596335211919='
r = requests.get(url=requrl,headers=header).text
res = json.loads(r)['data']    
for i,item in enumerate(res):
    if item:
        url = item['hoverURL']
    print(url)
    with open('/Users/fangfangyue/Downloads/test-pictures/{}.jpg'.format(i),'wb+') as f:
        f.write(requests.get(url).content)
