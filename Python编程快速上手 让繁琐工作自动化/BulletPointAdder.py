#! python3
# BulletPointAdder.py - 在Wiki标记中添加无序列表

import pyperclip

class BulletPointAdder:

    def __init__(self):
        pass

    def startAdd(self):
        text = pyperclip.paste()
        #TODO: 分割行并且添加星
        lines = text.split('\n')
        print(lines)
        for i in range(len(lines)): #通过索引循环lines列表
            lines[i] = '* ' + lines[i] #为每一个lines添加*
        text = '\n'.join(lines)
        pyperclip.copy(text)

if __name__ == '__main__':
    bp = BulletPointAdder()
    bp.startAdd() 