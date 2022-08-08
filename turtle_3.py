from turtle import*
painter = Turtle()

painter.pencolor("blue")
bgcolor('black')

for i in range(50):
    painter.forward(50)
    painter.left(123)  # Let's go counterclockwise this time

painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)

done()
