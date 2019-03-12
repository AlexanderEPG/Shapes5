#shapes 5 by APG
from graphics import*

diaSize = 50
winX = 600
winY = 600

win = GraphWin("5_shapes", winX, winY)
win.setCoords(0, 0, winX, winY)

#shape 1
c = Circle(Point(winX/winX + 50,winY/11.5), 50)
c.draw(win)
cornerPoint = c.getP1()
c.setFill("light blue")

#shape 2
o = Oval(Point(450,5), Point(595,100))
o.draw(win)
cornerPoint = o.getP1()
o.setFill("red")

#shape 3 
r = Rectangle(Point(1,595), Point(100,500)) 
r.draw(win)
cornerPoint = r.getP1()
r.setFill("green")
#shape 4
bTri = Polygon(Point(550 + diaSize, 550),
                Point(550 + diaSize, 550),
                Point(550, 550 - diaSize),
                Point(550, 550 + diaSize)) 

pointList = bTri.getPoints() 
               
bTri.draw(win)
bTri.setFill("black")


#shape 5
bDia = Polygon(Point(winX/2 + diaSize, winY/2),
                Point(winX/2 + diaSize, winY/2),
                Point(winX/2, winY/2 - diaSize),
                Point(winX/2, winY/2 + diaSize)) 

pointList = bDia.getPoints() 
               
bDia.draw(win)
bDia.setFill("black")
                
win.getMouse() # pause for click in window
win.close()


