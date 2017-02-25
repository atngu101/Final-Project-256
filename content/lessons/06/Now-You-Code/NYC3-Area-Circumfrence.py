'''
Now You Code 3: Area and Circumfrence

Write a program to input the radius of a cicle, then output the area
and circumfrence of that circle. Feel free to research the formulas online.

Requirements:

#1 Import the Python library math, so you can use the constant math.PI

#2 The program should handle bad input (entering non numerical values should
not cause a run-time error).

#3 Be sure to write two functions:

Function: calc_area
Arguments: radius
Returns: circle's area

Function: calc_circ
Arguments: radius
Returns: circle's circumfrence

Example Run #1:

    Enter Circle Radius : 1
    A circle with radius 1.000 has a
    Circumfrence of 6.283
    and an Area of 3.142

Example Run #2:

    Enter Circle Radius : r
    Invalid radius!

As usual start out your program by writing your TODO list of steps
you'll need to solve the problem!

'''

# TODO: Write Todo list then beneath write your code
# allow users to input their values
# define the function
# insert the circumfrence equation
# counter with a bad function 
# print everything


# Write code here 
import math
try:
    radius = int(input('Enter Circle Radius: '))

    def calc_area(radius):
        area = (math.pi) * (math.pow(radius, 2))
        return area
    def calc_circ(radius):
        circum = 2 * math.pi * radius
        return circum

    print('A cirle with radius', radius, 'has a') 
    print('Circumfrence of', '%.2f' % calc_circ(radius))
    print('and an Area of', '%.2f' % calc_area(radius))
    
except ValueError:
    print('Invalid Radius!')
