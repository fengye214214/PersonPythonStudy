import sys
import random
import copy
import pprint
import re
import os
import shelve
import myCats
import zipfile
import requests
import bs4


class MyPythonAuto:
    
    def __init__(self):
        pass

    def test(self):
        strLen = len('hello world!')
        #strLen = str(29)
        strBool = True
        print(strLen)

    def inputName(self):
        name = ''
        while name != 'name':
            print('Please type your name.')
            name = input()
        print('Thank you!')
    
    def testRange(self):
        for i in range(1, 10, 2):
            print(i)

    def spam(self,divideBy):
        try:
            return 42 /divideBy
        except ZeroDivisionError:
            print('Error: Invalid argument.')

    def testRange(self):
        L = ['1', '2', '3', '4', '5']
        del L[2]
        print(L)

    def testCatNames(self):
        catNames = []
        while True:
            print('输入猫的名字' + str(len(catNames) + 1) + '(或者输入回车停止)')
            name = input()
            if name == '':
                break
            catNames = catNames + [name] # list concatenation
            print('猫的名字是：')
            for name in catNames:
                print(' ' + name)

    def test421(self):
        supplies = ['pen', 'staplers', 'flame-throwers', 'binders']
        for i in range(len(supplies)):
            print('索引 ' + str(i) + ' in supplies is: ' + supplies[i])
        for name in supplies:
            print(name)
    
    def test422(self):
        myPets = ['Zophie', 'Pooka', 'Fat-tail']
        print('输入宠物名称：')
        name = input()
        if name not in myPets:
            print('I do not have a pet named' + name)
        else:
            print(name + 'is my pet.')

    def test433(self):
        cat = ['fat', 'black', 'lound']
        size, color, disposition = cat
        print(color)

    def test442(self):
        spam = ['cat', 'dog', 'bat']
        print(spam)
        spam.append('moose')
        print(spam)
        spam.insert(0, 'chicken')
        print(spam)
    
    def test444(self):
        spam = [2, 5, 3.14, 1, -7]
        print(spam)
        spam.sort(reverse = True)
        print(spam)
        spam1 = ['a', 'z', 'A', 'Z']
        spam1.sort(key = str.lower)
        print(spam1)

    def test5(self):
        print('Four score and seven' + \
              'years ago..')
        message= ['It is certain',
                  'It is decidedly so',
                  'Yes definitely',
                  'Vert doubtful']
        print(message[random.randint(0, len(message) - 1)])

    def test461(self):
        eggs = ['one', 'two', 'three']
        print(eggs)
        eggs.remove('one')
        print(eggs)
        del eggs[1]
        print(eggs)

    def test462(self):
        eggs = ('hello', 42, 0.5)
        print(type(eggs))
        singleEggs = ('hello',)
        print(type(singleEggs))

    def test463(self):
        ls = ['cat', 'dog', 5]
        print(ls)
        tu = tuple(ls)
        print(tu)
        ls1 = list(tu)
        print(ls1)

    def test472(self):
        spam = ['A', 'B', 'C', 'D']
        cheese = copy.copy(spam)
        cheese[1] = 42
        print(spam)
        print(cheese)

    def test51(self):
        myCat = {'size' : 'falt', 
                 'color' : 'gray',
                 'dispositiion' : 'loud'}
        print(myCat['color'])

    def test511(self):
        birthyDays = {'Alice' : 'Apr `',
                      'Bob' : 'Dec 12',
                      'Carol' : 'Mar 4',}
        print(birthyDays)

        while True:
            print('Enter a name: (blank to quit)')
            name = input()
            if name == '':
                break

            if name in birthyDays:
                print(birthyDays[name] + ' is the birthday of ' + name)
            else:
                print('I do not have birthday information for ' + name)
                print('What is their birthday?')
                body = input()
                birthyDays[name] = body
                print('Birthday database updated.')
                print(birthyDays)

    def test512(self):
        spam = {'color' : 'red', 'age' : 42}
        for v in spam.values():
            print(v)
        for k in spam.keys():
            print(k)
        for i in spam.items():
            print(i)
        print(list(spam.keys()))
        for k, v in spam.items():
            print('Key: ' + k + ' Value: ' + str(v))
        picnicItems = {'apples' : 5, 'cup' : 2}
        print(' I am bringing ' + str(picnicItems.get('cup', 0)) + 'cups.')

    def test515(self):
        spam = {'name': 'Pooka', 'age': 5}
        print(spam)
        spam.setdefault('color', 'black')
        print(spam)

    def characterCount(self):
        message = 'It was '
        count = {}
        for ch in message:
            count.setdefault(ch, 0)
            count[ch] = count[ch] + 1

        pprint.pprint(count)
        print(pprint.pformat(count))

    def printBoard(self, board):
        print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
        print('-+-+-')
        print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
        print('-+-+-')
        print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
        

    def ticTacToe(self):
        theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                    'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
        turn = 'X'
        for i in range(9):
            self.printBoard(theBoard)
            print('Turn for ' + turn + '.Move on which space?')
            move = input()
            theBoard[move] = turn
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        print(theBoard)

    def test532(self):
        allGuests = {'Alice': {'appkes': 5, 'pretzels': 12},
                    'Bob': {'ham sandwiches': 3, 'apples': 2},
                    'Carol': {'cups': 3, 'apple pies': 1}}
        numBrought = 0
        for k, v in allGuests.items():
            numBrought = numBrought + v.get('appkes', 0)
            print(numBrought)

    def test612(self):
        spam = "That is Alice's cat"
        spam1 = r'Say hi to Bob\'s mpther'
        spam2 = '''Dear Alice,
                Eve's cat has been arr
                Sincerely,
                Bob'''
        """
        注释
        """
        print(spam2)
    
    def test622(self):
        while True:
            print('Enter you age:')
            age = input()
            if age.isdecimal():
                break
            print('Please enter a number for your age.')

    def printPicnic(self, itemsDict, leftWidth, rightWidth):
        print('Hello'.center(leftWidth + rightWidth, '='))
        names = input()

    def testRe(self):
        phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}') #r表示原始字符，比如里面有\n,则\n就不表示转义字符，如果不加r\\表示转移字符
        mo = phoneNumRegex.search('My Number is 415-555-4242.My Number is 999-999-9999.')
        print('Phone number found: ' + mo.group())

    def testReGroup(self):
        phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{3})')
        mo = phoneNumRegex.search('My Number is 415-555-4242.is 999-999-9999.')
        print('Phone number found:' + mo.group(0))
        print('Phone number found:' + mo.group(1))
        print('Phone number found:' + mo.group(2))
        print('Phone number found:' + mo.group())

    def testGeGroups(self):
        phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{3})')
        mo = phoneNumRegex.search('My Number is 415-555-4242.is 999-999-9999.')
        test1, test2 = mo.groups()
        print(test1)
        print(test2)
        print(mo.groups())

    #管道匹配
    def testRePip(self):
        phoneNumRegex = re.compile(r'Tom|Tim'); #与关系，只要有一个匹配就自动匹配
        mo = phoneNumRegex.search('My name os T1om, and when is Tim')
        print(mo.group())
        
    #管道匹配多个分组
    def testReBat(self):
        phoneNumber = re.compile(r'Bat(man|mobile|as)')
        mo = phoneNumber.search('My name is  Batmobile Batas')
        print(mo.group())
        pn = re.compile(r'AA(11|22|33)')
        mo = pn.search('my name is  AA33')
        print(mo.group())

    #用问号实现可选匹配
    def testReIsSelect(self):
        pn = re.compile(r'An(wo)?man')
        mo = pn.search('The Adventures of Anman')
        print(mo.group())
        mo1 = pn.search('I am a Anwoman')
        print(mo1.group())
        #no1 = pn.search('I am a A Anwowowoman')
        #print(no1.group())

    #用星号匹配零次或多次
    def testReStart(self):
        pn = re.compile(r'Cd(wo)*man')
        mo = pn.search('The test Cdman')
        print(mo.group())
        no1 =pn.search('The test Cdwowowoman')
        print(no1.group())

    #用加好匹配一次或多次
    def testRePlus(self):
        pn = re.compile(r'ac(as)+man')
        mo = pn.search('The acasman')
        print(mo.group())
        mo1 = pn.search('The acasasman acasman')
        print(mo1.group())
    
    #用花括号匹配特定次数
    def testReHua(self):
        pn = re.compile(r'(ha){2}')
        no = pn.search('The haha')
        print(no.group())

    #7.4贪心和非贪心匹配
    def testReHeart(self):
        pn = re.compile(r'(Ha){3,5}')
        mo = pn.search('HaHaHaHaHaHa')
        print(mo.group())
        pn1 = re.compile(r'(Ha){3,5}?')
        mo1 = pn1.search('HaHaHaHaHaHa')
        print(mo1.group())

    #7.5findAll
    def testFindAll(self):
        phoneNumber = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
        mo = phoneNumber.search('phone1: 000-1111-2222. phone2: 222-8888-8888')
        print(mo.group())
        mo1 = phoneNumber.findall('phone1: 000-1111-2222. phone2: 222-8888-8888')
        print(mo1)

    #7.6字符分类
    #   \d 0到9的任何数字
    #   \s 空格、制表符或换行符（可以认为是匹配“空白”字符）
    #   \w任何字母、数字或下划线字符（可以认为是匹配“单词”字符）
    def testString(self):
        pn = re.compile(r'[0-5]')
        mo = pn.findall('123456789')
        print(mo)
        pn1 = re.compile(r'\d+\s\w+')
        mo1 = pn1.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids,' + \
                          ' 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
        print(mo1)

    #7.7建立自己的字符串分类
    def testMyString(self):
        voRegex = re.compile(r'[aeiouAEIOU]')
        pn = voRegex.findall('ma ne bi vo cu mA nE bI bO bU')
        print(pn)
        pn = re.compile(r'[a-zA-Z0-9]')
        mo = pn.findall('3435gfdf+|_')
        print(mo)
        pn1 = re.compile(r'[0-5\.]')
        mo1 =pn1.findall('123456789ADX.')
        print(mo1)
        voRe1 = re.compile(r'[^aeiouAEIOU]')
        pn2 = voRe1.findall('ma ne bi vo cu mA nE bI bO bU')
        print(pn2)
    
    #7.8插入字符和美元
    def testStringAndDo(self):
        vo = re.compile(r'^Hello') #字符串必须以Hello开头
        pn = vo.search('Hello World!')
        print(pn.group())
        vo1 = re.compile(r'\d$')
        pn1 = vo1.search('Hello World! 323')
        print(pn1.group())
        vo2 = re.compile(r'^Hello\d$')
        pn2 = vo2.search('Hello3')
        print(pn2)
        vo3 = re.compile(r'^\d+$')
        pn3 = vo3.search('323232A32')
        print(pn3)

    #7.9通配字符
    def testAllString(self):
        no = re.compile(r'.at')
        res = no.findall('Iamat a am a ats at1 at2')
        print(res)

    #7.9.1用点星匹配所有字符
    #.(句点)匹配除了换行符以外的所有字符
    def testStartAllString(self):
        no = re.compile(r'First Name: (.*) Last Name: (.*)')
        res = no.search('First Name: AA Last Name: VV')
        print(res.group())
        no1 = re.compile(r'<.*?>')
        res1 = no1.search('<To serve man> for dinner.>')
        print(res1.group())
        no2 = re.compile(r'<.*>')
        res2 = no2.search('<To serve man> for dinner.>')
        print(res2.group())

    #7.9.2用句点字符匹配换行符
    def test792(self):
        no = re.compile('.*')
        res = no.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
        print(res.group())
        print('*************************')
        no1 = re.compile('.*', re.DOTALL)
        res1 = no1.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
        print(res1.group())

    #7.11不分大小写的匹配
    def testAllWord(self):
        no = re.compile('robocop',re.I)
        res =no.search('RoboCop is part man, part machine, all cop.')
        print(res.group())
        res1 = no.search('ROBOCOP is part man, part machine, all cop.')
        print(res1.group())

    #7.12用sub()方法替换字符串
    def testSub(self):
        no = re.compile(r'Agent \w+')
        res = no.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.')
        print(res)
    
    def testSubEx(self):
        no = re.compile(r'Agent (\w)\w*')
        res = no.findall('Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
        print(res)
        print('*********')
        res1 = no.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
        print(res1)

    #7.13管理复杂的正则表达式
    def testComplexRe(self):
        pn = re.compile(r'''
            (\d{3}|\(\d{3}\))?             #area code
            (\s|-|\.)?                     #separator
            \d{3}                          #first 3 digits
            \d{4}                          #last 4 digits
            (\s*(ext|x|ext.)\s*\d{2,5})?   #extension
            ''')
        on1 = re.compile('fool', re.IGNORECASE | re.DOTALL)
        on2 = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
        te = re.compile(r'[a-z]{2,4}')
        mo = te.findall('asdfghj')
        print(mo)
        print(mo[0])
        print(mo[1])

    #8.1文件及路径
    def testOSPath(self):
        myFiles = ['account.txt', 'details.csv', 'test.docx']
        for fileName in myFiles:
            print(os.path.join('C:\\Users\\fengye', fileName))
        print(os.getcwd())
        os.chdir('C:\\')
        print(os.getcwd())
        os.makedirs('C:\\delicious\\walnut\\waffles')

    #8.2读取文件
    def testReadFile(self):
        helloFile = open('C:\\test.txt')
        helloContent = helloFile.read()
        print(helloContent)
        
    #8.3文件写入
    def testWriteFile(self):
        helloFile1 = open('C:\\test1.txt','w') #a
        helloFile1.write('Hello world!2\n')
        helloFile1.close()

    #8.3用shelve模块保存变量
    def testShelveFile(self):
        shelfFile = shelve.open('mydata')
        cats = ['Zophie', 'Pooka', 'Simon']
        shelfFile['cats'] = cats
        shelfFile.close()

    def testShelveRead(self):
        sf = shelve.open('mydata')
        type(sf)
        print(sf['cats'])
        sf.close()

    #8.4用pprint.pformat()函数保存变量
    def testpprintformat(self):
        cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
        re = pprint.pformat(cats)
        print(re)
        fileObj = open('myCats.py', 'w')
        fileObj.write('cat = ' + pprint.pformat(cats) + '\n')
        fileObj.close()

    def testMyCats(self):
        no = myCats.cat
        print(no)
        m = ['a']
        n = ['b']
        print(m  + n)

    #9.1 shutil.copy
    #    shutil.cpoytree
    #    shutil.move
    #    shutil.unlike
    #    shutil.rmdir
    #    shutil.rmtree

    #9.2遍历目录书
    def testListTree(self):
        for folderName, subfolders, filenames in os.walk('G:\\Windows 10 x64'):
            print('当前目录文件夹是%s' % (folderName))

            for subFolder in subfolders:
                print('SUBFOLDER OF ' + folderName + ': ' + subFolder)
            for fileName in filenames:
                print('FILE INSIDE ' + folderName + ': '+ fileName)

            print('')

    #9.3测试ZIP文件
    def testZIP(self):
        os.chdir('C:\\')
        exampleZip = zipfile.ZipFile('example.zip')
        re = exampleZip.namelist()
        print(re)
        re1 = exampleZip.getinfo('testCo.txt')
        print(re1.file_size)
        print(re1.compress_size)
        exampleZip.close()

    #9.3.2从ZIP中解压文件
    def testUnZIP(self):
        os.chdir('C:\\')
        exampleZip = zipfile.ZipFile('example.zip')
        exampleZip.extractall()
        exampleZip.close()

    #9.3.3创建和添加到ZIP
    def testAZIP(self):
        newZIP = zipfile.ZipFile('new.zip', 'w')
        newZIP.write('PythonAuto.py', compress_type = zipfile.ZIP_DEFLATED)
        newZIP.close()

    #10.1异常测试
    def testException(self):
        print('ok')
        raise Exception('异常测试...')
        print('ok1')

    def testAssert(self):
        podBayDoorStatus = 'open'
        assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
        
    def testPrint(self):
        print('ok')

    11.4
    def testRequest(self):
        res = requests.get('https://www.baidu.com/')
        try:
            res.raise_for_status()
        except Exception as exc:
            print('异常：%s' % (exc))
        print(type(res))
        print(res.status_code == requests.codes.ok)
        print(len(res.text))
        #print(res.text)
        playFile = open('RomeoAndJuliet.txt', 'wb')
        for chunk in res.iter_content(10000):
            playFile.write(chunk)
        playFile.close()

    def testHTML(self):
        res = requests.get('http://www.dytt8.net/')
        res.raise_for_status()
        #resStr = res.content.decode('gbk', 'ignore')
        #print(resStr)
        print(res.text.encode('utf-8', 'ignore').decode('gbk', 'ignore'))
        noStarchSoup = bs4.BeautifulSoup(resStr, 'html.parser')
        #type(noStarchSoup)
        elems = noStarchSoup.select('#co_content8')
        #type(elems)
        #print(len(elems))
        #print(elems[0])
        
        
        
if __name__ == '__main__':
    my = MyPythonAuto()
    my.testHTML()
    
    '''
    def testPrintEggs():
        global eggs
        eggs = 'spam'

    eggs = 'global'       
    testPrintEggs()
    print(eggs)
    '''

    
    #让程序自动退出
    #sys.exit()