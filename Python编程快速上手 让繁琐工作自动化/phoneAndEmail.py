#! python3
#  phoneAndEmail.py - 在剪切板中寻找电话号码和Email地址-Find phone numbers and emails address on the clipboard

import pyperclip, re

#电话号码正则表达式
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?          #area code 区号可能只是 3 个数字（即\d{3}）， 或括号中的 3 个数字（即\(\d{3}\)）
    (\s|-|\.)?                  #seperator 电话号码分割字符可以是空格（\s）、 短横（-） 或句点（.）
    (\d{3})                     #first 3 digits
    (\s|-|\.)                   #separator
    (\d{4})                     #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension
    )''', re.VERBOSE)
#email正则表达式
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           #username
    @                           #@ symbol
    [a-zA-Z0-9.-]+              #domain name
    (\.[a-zA-Z]{2,4})           #dot-something
    )''', re.VERBOSE)
#Find matches in clipboard text.
text = str(pyperclip.paste())
matchs = []
#匹配电话号码
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matchs.append(phoneNum)
#匹配Email
for groups in emailRegex.findall(text):
    matchs.append(groups[0])
#复制结果到剪切板
if len(matchs) > 0:
    pyperclip.copy('\n'.join(matchs))
    print('Copied to clipboard:')
    print('\n'.join(matchs))
else:
    print('没有电话号码或者Email地址被发现')
