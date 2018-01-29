#! python3
# mapIt.py 利用 webbrowser 模块

import webbrowser, sys, pyperclip 

if len(sys.argv) > 1:
    #从命令行获取地址
    address = ' '.join(sys.argv[1:])
else:
    #从剪切板获取地址
    address = pyperclip.paste()

#打开浏览器
webbrowser.open('http://www.google.cn/maps/place/' + address)


