from urllib.request import urlopen

url='http://www.baidu.com'

resp = urlopen(url).read().decode('utf8')
print(resp)
