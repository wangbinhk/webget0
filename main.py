import requests
res = requests.get('http://www.zou114.com/sanzidaima/index.asp?zm=a&page=1')
res.encoding = 'gb2312'
print(res.text)