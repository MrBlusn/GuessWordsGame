from graphics import *
import GuessProgress
win=GraphWin("WELCOME",400,300)
win.setBackground("grey")

btnNew=Rectangle(Point(50,50),Point(350,150))
btnNew.setFill('white')
btnNew.draw(win)

Connet=Text(Point(200,100),'hello')
Connet.setTextColor('black')
Connet.draw(win)


txtPos1=Text(Point(200,30),'Click NEW to start a game')
txtPos1.setTextColor('black')
txtPos1.draw(win)

txtPos2=Text(Point(200,170),'WELCOME TO THE GUESS MASTER!')
txtPos2.setTextColor('black')
txtPos2.draw(win)

btnNew1=Rectangle(Point(50,200),Point(110,240))
btnNew1.setFill('yellow')
btnNew1.draw(win)
txtPos3=Text(Point(80,220),'NEW')
txtPos3.setTextColor('black')
txtPos3.draw(win)

btnNew2=Rectangle(Point(290,200),Point(350,240))
btnNew2.setFill('black')
btnNew2.draw(win)
txtPos4=Text(Point(320,220),'QUIT')
txtPos4.setTextColor('yellow')
txtPos4.draw(win)

btnNew3=Rectangle(Point(0,255),Point(400,285))
btnNew3.setFill('black')
btnNew3.draw(win)
txtPos4=Text(Point(200,270),'GUESS MASTER 2.0')
txtPos4.setTextColor('yellow')
txtPos4.draw(win)

while True:
    p=win.getMouse()
    p1=btnNew1.getP1()
    p2=btnNew1.getP2()
    p3=btnNew2.getP1()
    p4=btnNew2.getP2()
    if p1.x<=p.x<=p2.x and p1.y<=p.y<=p2.y:
        win.close()
        GuessProgress.Guess()
    elif p3.x<=p.x<=p4.x and p3.y<=p.y<=p4.y:
        win.close()
