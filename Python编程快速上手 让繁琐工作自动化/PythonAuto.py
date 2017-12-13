import sys

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


if __name__ == '__main__':
    my = MyPythonAuto()
    #my.InputName()
    #my.testRange()
    #my.testFunction('hello world!')
    #noes = None
    #print(noes)
    #my.testPrintEggs()
    #print(my.spam(0))
    my.testRange()
    
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