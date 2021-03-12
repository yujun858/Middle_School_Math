import requests

word = input('输入翻译单词:')

url = 'https://fanyi.baidu.com/sug'

data = {'kw':word}

resp = requests.post(url,data=data)

print(resp.json())
