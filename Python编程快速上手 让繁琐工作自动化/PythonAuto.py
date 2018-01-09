import sys
import random
import copy  

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
        
        

if __name__ == '__main__':
    my = MyPythonAuto()
    my.test511()
    
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