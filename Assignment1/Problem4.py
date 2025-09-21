import turtle as t

t.speed(1000)
t.hideturtle()
t.penup()
t.goto(400, -400)
t.pendown()
t.left(180)
step = 1
for i in range(100):
    t.forward(9 * step)
    t.right(90)
    t.forward(9 * step)
    t.right(90)
    t.forward(9 * step)
    t.right(90)
    t.forward(9 * step)
    t.right(90)
    step += 1
t.done()
