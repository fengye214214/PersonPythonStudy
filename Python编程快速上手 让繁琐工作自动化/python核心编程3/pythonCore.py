# python3
# pythonCore.py python核心编程

import re
import os

class pythonCore:

    def __init__(self):
        pass

    def testPrint(self):
        print('test ok')

    #1.3.4 使用match()方法匹配字符串
    def testMatch(self):
        m = re.match('foo', 'foo')
        if m is not None:
            print(m)
            print(m.group())

    def testMatch1(self):
        res = re.match('foo', 'foo on the table').group()
        print(res)

    #1.3.5使用search()在一个字符串中查找模式（搜索与匹配的对比）
    def testSearch(self):
        m = re.search('foo', 'seafood')
        if m is not None:
            print(m.group())
    
    #1.3.6匹配多个字符串
    def testMatchMany(self):
        bt = 'bat|net|bit'
        m = re.match(bt, 'bat')
        if m is not None:
            print(m.group())

        m = re.match(bt, 'He bit me!')
        if m is not None:
            print(m.group())
        else:
            print('not match')
            
        m = re.search(bt, 'He bit me!')
        if m is not None:
            print(m.group())

    #1.3.7 匹配任何单个字符
    def matchAnySingleStr(self):
        anyend = '.end'
        m = re.match(anyend, 'bend')
        if m is not None:
            print(m.group())
        
        m = re.match(anyend, 'end') #不匹配任何字符
        if m is not None:
            print(m.group())
        else:
            print('None')

        m = re.match(anyend, '\nend') #除了\n之外的任何字符
        if m is not None:
            print(m.group())
        else:
            print('None')
        
        m = re.search('.end', 'The end.') #在搜索中匹配' '
        if m is not None:
            print(m.group())
        else:
            print('None')

        m = re.search('3\.14', '3.14') #匹配小数点
        if m is not None:
            print(m.group())
        else:
            print('not point')

        test314 = '3.14'
        m = re.match(test314, '3014') #点号匹配0
        if m is not None:
            print(m.group())
        else:
            print('None')

        m = re.match(test314, '3.14') #点号匹配'.'
        if m is not None:
            print(m.group())
        else:
            print('None')

    #1.3.8 创建字符集([])
    def testCreateStrings(self):
        m = re.match('[cr][23][dp][o2]', 'c3po') #匹配c3po
        if m is not None:
            print(m.group())
        
        m = re.match('r2d2|c3po', 'c2do')
        if m is not None:
            print(m.group())
        else:
            print('None')

        m = re.match('r2d2|c3po', 'r2d2')
        if m is not None:
            print(m.group())
        else:
            print('None')
        
    #1.3.9 重复、特殊字符以及分组
    def testRepetSpecialGroup(self):
        patt = '\w+@\w+\.com'
        m = re.match(patt, '123@qq.com')
        if m is not None:
            print(m.group())
        else:
            print('None')

        exPatt = '\w+@(\w+\.)?\w+\.com'
        m = re.match(exPatt, '123@www.xxx.com')
        if m is not None:
            print(m.group())
        else:
            print('None')     

        exPatt1 = '\w+@(\w+\.)*\w+\.com'
        m = re.match(exPatt1, '123@www.qqqq.ccc.com')
        if m is not None:
            print(m.group())

        m = re.match('\w\w\w-\d\d\d', 'abc-123')
        if m is not None:
            print(m.group())

        m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
        if m is not None:
            print(m.groups())
            print(m.group())
            print(m.group(1))
            print(m.group(2))

    def testRepetSpecialGroup1(self):
        m = re.match('ab', 'ab')
        print(m.group())
        print(m.groups())

        m = re.match('(ab)', 'ab')
        print(m.group())
        print(m.group(1))
        print(m.groups())

        print('\n')
        m = re.match('(a(b))', 'ab')
        print(m.group())
        print(m.group(1))
        print(m.group(2))
        print(m.groups())

    #1.3.10 匹配字符串的起始和结尾及单词边界
    def testMatchStringStartAndEnd(self):
        m = re.search('^The', 'The end.')
        if m is not None:
            print(m.group())

        print('在边界')
        m = re.search(r'\bthe', 'bitethe dog')
        if m is not None:
            print(m.group())

        m = re.search(r'\Bthe', 'bitethe dog')
        if m is not None:
            print(m.group())

    #1.3.11 使用 findall()和 finditer()查找每一次出现的位置
    def testFindallAndfinditer(self):
        m = re.findall('car', 'carry the barcardi to the car')
        print(m)
        print('findall')
        s = 'This and that.'
        m = re.findall(r'(th\w+) and (th\w+)', s, re.I)
        print(m)
        print('finditer')
        m = re.finditer(r'(th\w+) and (th\w+)', s, re.I)
        for i in m:
            print(i.group())

    #1.3.12 使用sub()和subn()搜索与替换
    def testSubAndSubn(self):
        oldStr = 'attn:X\n\nDear X, \n'
        print(oldStr)
        m = re.sub('X', 'Mr. Smith', oldStr)
        print(m)
        m = re.subn('X', 'Mr. Smith', oldStr)
        print(m)
        m = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',r'\2/\1/\3', '2/20/91')
        print(m)

    #1.3.13 在限定模式上使用 split()分隔字符串
    def testSplit(self):
        DATA = {
            'Mountain View, CA 94040',
            'Sounnyvalue, CA',
            'Cupertino 95012',
            'Palo Alto CA',
        }
        for datum in DATA:
            print(re.split(', |(?= (?:\d{5}|[A-Z]{2}))', datum))

    #1.3.14 扩展符号
    def testExtendSymbol(self):
        res = re.findall(r'(?i)yes','yes? Yes. YES!!')
        print(res)
        res = re.findall(r'(?i)th\w', 'The quickest way is through this tuunnel.')
        print(res)
        res = re.findall(r'(?im)(^th[\w ]+)', """
                        This line is the first,
                        another line,
                        that line, it's the best
                        """)
        print(res)
        res = re.findall(r'th.+', '''
                        The first line
                        the second line
                        the third line
                        ''')
        print(res)
        res = re.findall(r'(?s)th.+','''
                        The first line
                        the second line
                        the third line
                        ''')
        print('1' + str(res))
        res = re.search(r'''(?x)
                    \((\d{3})\) #区号
                    [ ] #空白符
                    (\d{3}) #前缀
                    -      #横线
                    (\d{4}) #终点数字
                    ''', '(800) 555-1212').groups()
        print(res)
        res = re.findall(r'http://(?:\w+\.)*(\w+\.com)',
                        'http://google.com http://www.google.com http://code.google.com')
        print(res)
        res = re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '(800) 555-1212').groupdict()
        print(res)
        res = re.findall(r'\w+(?= van Rossum)',
                        '''
                        Guido van Rossum
                        Tim Pters
                        Alex Martelli
                        Just van Rossum
                        Raymoud Hettinger
                        ''')
        print(res)
        
        
    def reWho(self):
        with os.popen('whodata.txt', 'r') as f:
            for eachLine in f:
                print(re.split(r'\s\s+', eachLine.strip()))
    
    def retasklist(self):
        with open('ta.txt', 'r') as f:
            for eachLine in f:
                print(re.split(r'\s\s+|t', eachLine.strip()))

        
#启动函数           
if __name__ == '__main__':
    pc = pythonCore()
    pc.reWho()