import turtle

#turtle.circle(50,180)

turtle.color("Red", "Blue")
turtle.shape("turtle")
turtle.begin_fill()

print("drawing a Sqaure")

for t in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.end_fill()


turtle.getscreen()._root.mainloop()