from graphics import *
import random


datafile = open("data.txt",'r') # Read in and print out the data in the data file
bigData = datafile.readlines()


window = GraphWin("Visualisation", 600, 600) # Create a window for all the drawings

for line in bigData: #function to draw different colours and sizes rectangles
	print(line)
	box = Rectangle(Point(random.randint(1,600),random.randint(1,600)),Point(300,300))
	box.setOutline(color_rgb(150,150,150))
	box.setFill(color_rgb(random.randint(1,200),84,95))
	box.draw(window)

for line in bigData: #function to draw different colours and sizes circles
	print(line)
	ball = Circle(Point(random.randint(1,600),random.randint(1,600)),float(line))
	ball.setFill(color_rgb(random.randint(1,200),80,0))
	ball.draw(window)

# for line in bigData:
# 	print(line)
# 	line = Line(Point(300,float(line)),Point(300,280))
# 	line.setWidth(2)
# 	line.draw(window)

# text = Text(Point(50,200),"Hello")
# text.draw(window)

# Waits until the mouse is clicked before closing the window
window.getMouse()
