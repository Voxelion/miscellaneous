import turtle

window = turtle.Screen()
mario = turtle.Turtle()

window.bgcolor('white')
window.title('Super Mario Bros')

mario.color('red')
mario.pensize(1)

mario.forward(50)
mario.left(90)
mario.forward(30)
mario.right(60)
mario.forward(100)

window.mainloop()
