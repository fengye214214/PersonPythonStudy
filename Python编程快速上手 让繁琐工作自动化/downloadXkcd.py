#! python3
# downloadXkcd.py 下载所有XKCD漫画

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok=True) #注意与mkdirs的区别
while not url.endswith('#'):
    #下载页面
    print('下载页面 %s' % url)
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as ex:
        print(ex)
    #获取标签
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #寻找id为comic的div图片
    comicELem = soup.select('#comic img')
    if comicELem == []:
        print('没有找到图片')
    else:
        #print(comicELem)
        comicUrl = 'http:' + comicELem[0].get('src')
        #print(comicUrl)
        #下载图片
        print('下载图片%s' % (comicUrl))
        res = requests.get(comicUrl)
        try:
            res.raise_for_status()
        except Exception as ex:
            print('下载图片异常%s' % (ex))
        #下载图片到./xkcd文件夹下
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

        #寻找上一页按钮的url
        prevLink = soup.select('a[rel="prev"]')[0]
        #print(prevLink)
        url = 'http://xkcd.com' + prevLink.get('href')
        #print(url)
print('下载完成...')