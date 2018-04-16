# python.py
# CircleTurtle.py

import math
import turtle

def drawCircleTurtle(x, y, r):
    #开始第一个圆
    turtle.up()
    turtle.setpos(x + r, y)
    turtle.down()


class Spiro:
    #构造函数
    def __init__(self, xc, yc, col, R, r, l):
        #创建turtle对象
        self.t = turtle.Turtle()
        #设置图标
        self.t.shape('turtle')
        #在度数上设置
        self.step = 5
        #设置会话的完全项
        self.drawingComplete = False
        #设置参数
        self.setpParams(xc, yc, col, R, r, l)
        #初始化drawing
        self.restart()

    #设置参数
    def setparams(self, xc, yc, col, R, r, l):
        #Spirograph参数
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col
        #reduce r/R to its smallest from by diving with the GCD
        gcdVal = gcd(self.r, self.R)
        self.nBot = self.r // gcdVal
        #get ratio of ardii
        self.k = r /float(R)
        #set the color
        self.t.color(*col)
        #store the current angle
        self.a = 0

    #重画
    def restart(self):
        #设置flag
        self.drawingComplete = False
        #显示turtle
        self.t.showturtle()
        #到第一个点
        self.t.up()
        R, k, l = self.R, self.k, self.l
        a = 0.0
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()

    #画全部的事情
    def draw(self):
        R, k, l = self.R, self.k, self.l
        for i in range(0, 360 * self.nRot + 1, self.step):
            a = math.radians(i)
            x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
            y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
            self.t.setpos(self.xc + x, self.yc + y)
        #draw is now done so hide the turtle cursor
        self.t.hideturtle()

    #一步一步更新
    def update(self):
        #skip the rest of the setps if done
        if self.drawingComplete:
            return
        #increment the angle
        self.a += self.step
        #draw a step
        R, k, l = self.R, self.k, self.l
        #设置angle
        a = math.radians(self.a)
        x= self.R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = self.R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y
        # if drawing is complete, set the flag
        if self.a >= 360*self.nRot:
            self.drawingComplete = True
            # drawing is now done so hide the turtle cursor
            self.t.hideturtle()

    #开始花园

if __name__ == '__main__':
    drawCircleTurtle(100, 100, 50)
    turtle.mainloop()
    