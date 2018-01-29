#! python3
# lucky.py 用百度浏览器打开搜索结果,用命令行参数运行脚本，只有一个参数就是要搜索的内容
# py.exe G:\培训\pythonStudy\PersonPythonStudy\Python编程快速上手 让繁琐工作自动化 lucky.py 博客园
# 记得在脚本的当前目录下运行命令行
# 13:01 2018/1/26
# fengye 
# 578797371@qq.com
# 18220595312

import webbrowser, sys, requests, bs4, pprint

headers = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
}

print('百度ing...')
searchStr = 'https://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:])
print('搜索地址 %s' % (searchStr))
res = requests.get(searchStr,headers=headers)
try:
    res.raise_for_status()
except Exception as exc:
    print('异常 %s' % (exc))
#写入文件
playFile = open('lucky.txt', 'wb')
for chunk in res.iter_content(10000):
    playFile.write(chunk)
playFile.close()
#print(res.text)
#提取链接地址
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElements = soup.select('div[class="c-tools"]')
numOpen = min(5, len(linkElements)) #打开5个
for i in range(numOpen):
    dataLink = eval(linkElements[i].attrs['data-tools']) #eval字符串转字典
    print(dataLink['url'])
    webbrowser.open(dataLink['url'])
