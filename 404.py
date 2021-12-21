import turtle

def tree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15)
        t.left(40)
        tree(branch_len - 15)
        t.right(20)
        t.backward(branch_len)


if __name__ == '__main__':
    t = turtle.Turtle()
    t.left(90)
    t.penup()
    t.backward(300) # 100
    t.pendown()
    t.pencolor('green')
    t.pensize(2)
    tree(130) # 75
    t.hideturtle()
    turtle.done()
