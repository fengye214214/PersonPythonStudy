#! python3
# testSelenium.py 测试selenium，本脚本用的chrome浏览器，首先在ExPackages文件夹下找到chromedriver.zip，
# 把解压后的exe放到谷歌浏览器的安装目录下，然后再把谷歌浏览器的路径配置到环境变量的PATH中
# 或者直接填写r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'路径
# 此脚本用的是2.35 chromedriver.exe

from selenium import webdriver

def testFindElement():
    #option = webdriver.ChromeOptions()
    #option.add_argument('--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\Google\\Chrome\\User Data') #设置成用户自己的数据目录
    wb = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',chrome_options=None)
    type(wb)
    wb.get('https://www.baidu.com/')
    try:
        elem = wb.find_element_by_name('tj_trmap')
        print('查找到地图超链接%s' % (elem.tag_name))
        elem.click()
    except:
        print('没有匹配的元素！')

def testSubmitForm():
    wb = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    wb.get('https://www.baidu.com/')
    try:
        elem = wb.find_element_by_id('kw') #寻找输入搜索文字的文本框
        elem.send_keys('csdn')
        print(elem.tag_name)
        raw = input()
    except Exception as ex:
        print(ex)

#testFindElement()
testSubmitForm()