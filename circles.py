from turtle import *

# change colors :
colors = ["brown2", "lime", "red", "blue", "skyblue", "gold"]

bgcolor("black")
pensize(2)
speed(0)
delay(0)
ht()

for i in range(100):
	for j in range(6):
		color(colors[j % len(colors)])
		circle(5 * (i + 1) + 10)
		lt(60)
done()
