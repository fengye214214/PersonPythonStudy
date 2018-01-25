#! python3
# renameDates.py - 把美国日期格式MM-DD-YYYY修改为中国日期格式YYYY-MM-DD

import shutil, os, re

#创建一个正则表达式匹配美国日期
datePattern = re.compile(r'''^(.*?)  #所有文本在日期前面 .匹配所有字符换行符除外 ^必须以.匹配的字符开头
    ((0|1)?\d)-                      #月可能有一个或两个数字。用问号实现可选匹配，因为不一定有0和1
    ((0|1|2|3)?\d)-                  #日可能有一个或两个数字
    ((19|20)\d\d)                    #年有四个数字
    (.*?)$                           #所有文本在日期后面
    ''', re.VERBOSE)
reFilePath = '.\TempFiles'
#在工作目录下遍历文件
for amerFileName in os.listdir(reFilePath):
    mo = datePattern.search(amerFileName)
    #如果文件没有日期则继续
    if mo == None:
        continue

    #获取不同的文件名
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    #获取中国格式的文件名
    chinaFilename = beforePart + yearPart + '-' + monthPart + '-' + dayPart + afterPart
    #获取文件绝对路径
    absWorkingDir = os.path.abspath(reFilePath)
    amerFilename = os.path.join(absWorkingDir, amerFileName)
    chainaFilename = os.path.join(absWorkingDir, chinaFilename)
    #重命名文件
    print('改名 "%s" 到 "%s...' % (amerFilename, chainaFilename))
    #改名
    shutil.move(amerFilename, chainaFilename)
