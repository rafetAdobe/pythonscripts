from graphics import *
win = GraphWin("These are tests",width = 400, height = 400) # create a window

win.setCoords(0, 0, 100, 100) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)
win.setBackground("yellow")

for i in range(1,99):
    mySquare = Rectangle(Point(i, i), Point(99, 99))
    myOval = Oval(Point(i,i), Point(50,50))
    myOval.draw(win)
    # create a rectangle from (1, 1) to (9, 9)
    mySquare.draw(win) # draw it to the window
#win.plot(35, 128, "blue")    
win.getMouse() # pause before closing