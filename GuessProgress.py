from graphics import *
from random import *
from math import*
from time import*


def Guess():
    win2 = GraphWin('GUESS MASTER', 400, 300)
    win2.setBackground('orange')

    wordfile = open('words.txt', 'r')
    words = wordfile.readlines()
    word = choice(words)
    letterNum = len(word)-1
    print(letterNum)
    LETTER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']

    # 作26个黑色按钮组bot,填入26个字母letter
    bot=[]
    letter=[]
    for j in range(2):
        for i in range(13):
            bot.append(Circle(Point(20 + 30 * i, 245 + 30 * j), 15))
            bot[i+13*j].setFill('black')
            bot[i+13*j].draw(win2)

            letter.append(Text(Point(20 + 30 * i, 245 + 30 * j), LETTER[13 * j + i]))
            letter[i+13*j].setFill('white')
            letter[i+13*j].draw(win2)

    #构造字母p，Bot对应组成p的四边块
    Bot=[0,1,2,3,4,5,6,7,8,9]
    for i in range(10):
        if i==0:
         Bot[i] = Polygon(Point(155, 170), Point(215, 170), Point(210, 200), Point(150, 200))
         Bot[i].setFill('black')
         Bot[i].draw(win2)
        elif 0<i<=4:
            Bot[i]=Polygon(Point(165+5*(i-1), 170-30*i), Point(215+5*(i-1), 170-30*i),
                           Point(210+5*(i-1), 200-30*i), Point(160+5*(i-1), 200-30*i))
            Bot[i].setFill('black')
            Bot[i].draw(win2)
        elif 4<i<=6:
            Bot[i] = Polygon(Point(230+50*(i-5), 50), Point(230+50*(i-4), 50),
                             Point(225+50*(i-4), 80), Point(225+50*(i-5),80))
            Bot[i].setFill('black')
            Bot[i].draw(win2)
        elif 6<i<=7:
            Bot[i] = Polygon(Point(275 , 80), Point(325 , 80),
                             Point(320 , 110), Point(270 , 110))
            Bot[i].setFill('black')
            Bot[i].draw(win2)
        elif 7< i <= 9:
            Bot[i] = Polygon(Point(270-50*(i-8),110), Point(320-50*(i-8),110),
                             Point(315-50*(i-8), 140), Point(265-50*(i-8), 140))
            Bot[i].setFill('black')
            Bot[i].draw(win2)



    #单词框btn
    for i in range(letterNum):
        btn = Rectangle(Point(200-15*letterNum+30*i, 10), Point(230-15*letterNum+30*i, 40))
        btn.setFill('orange')
        btn.draw(win2)

    # 总结分数
    score=10
    scorewords = 'SORCE:{}'.format(score)
    Overwords = Text(Point(300, 200), scorewords)
    Overwords.setFill('black')
    Overwords.draw(win2)

    #获取所点字母
    Word=word[:]     #复制抽取的单词
    Getletter=''
    w = 0            #记录猜单词失败的次数
    while True:
        p = win2.getMouse()

        for j in range(2):
          for i in range(13):
             #判断鼠标落点是否在按钮上
             dx=20+30*i-p.x
             dy=245+30*j-p.y
             f=dx*dx+dy*dy
             m=sqrt(f)
             if m<=15:
               Getletter=LETTER[i+13*j]
               bot[i + 13 * j].setFill('orange')
               letter[i + 13 * j].setFill('black')


        if Getletter not in Word:
            score-=1
            Overwords.undraw()   #删除旧的分数

            scorewords = 'SORCE:{}'.format(score)
            Overwords = Text(Point(300, 200), scorewords)
            Overwords.setFill('black')
            Overwords.draw(win2) #打印新的分数

            # 移动p块
            Bot[w].setFill('white')
            rep1 = Bot[w].clone()
            rep1.setFill('red')
            rep1.draw(win2)
            w=w+1
            for i in range(20):
                sleep(0.01)
                rep1.move(-5 * i, 0)


        #填入字母
        while Getletter in Word:
           point = Word.find(Getletter)
           Word = Word[:point] + '0' + Word[point + 1:]

           x=(200-15*letterNum+30*point+230-15*letterNum+30*point)/2
           lerprint= Text(Point(x, 25), Getletter)
           lerprint.setTextColor('black')
           lerprint.draw(win2)
           break


        #结束语
        if Word.count('0')==letterNum:
            overwords=''' The word was :{}
        Congrating!!!'''.format(word)
            Overwords=Text(Point(70,90),overwords)
            Overwords.setFill('blue')
            Overwords.draw(win2)
            break
        elif w==10:
            overwords = ''' Sorry,
        the word was :{}'''.format(word)
            Overwords = Text(Point(70, 90), overwords)
            Overwords.setFill('blue')
            Overwords.draw(win2)


    win2.getMouse()