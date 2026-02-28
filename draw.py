import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("green")

# Move it so we see it
t.forward(100)
t.right(90)
t.forward(100)

# Keep the window open
turtle.done()
screen = turtle.Screen()
screen.getcanvas().winfo_toplevel().attributes("-topmost", True)