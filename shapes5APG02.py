#shapes 5 by APG
from graphics import*

diaSize = 30
winX = 600
winY = 600

#shape 1
win = GraphWin("5_shapes", winX, winY)
c = Circle(Point(winX/winX + 50,winY/11.5), 50)
c.draw(win)
cornerPoint = c.getP1()

#shape 2
o = Oval(Point(450,5), Point(595,100))
o.draw(win)
cornerPoint = o.getP1()

#shape 3 

win.getMouse() # pause for click in window
win.close()


