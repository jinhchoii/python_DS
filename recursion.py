"""
This is the example file for Recursion concept
Chloe Huang
July, 2021
"""

import turtle

MAX_LENGTH = 200
INCREMENT = 50


def draw_spiral(a_turtle, line_length):
    # Base Case
    if line_length > MAX_LENGTH:
        return

    # Small Problem
    a_turtle.forward(line_length)
    a_turtle.right(90)

    # Call itself recursively 
    draw_spiral(a_turtle, line_length + INCREMENT)

bob = turtle.Turtle(shape="turtle")
bob.pensize(5)
bob.color("red")
draw_spiral(bob, 10)
turtle.done
