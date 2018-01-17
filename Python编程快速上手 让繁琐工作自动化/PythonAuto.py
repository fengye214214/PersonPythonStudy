import sys
import random
import copy
import pprint
import re

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
        

if __name__ == '__main__':
    my = MyPythonAuto()
    my.testReIsSelect()
    
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