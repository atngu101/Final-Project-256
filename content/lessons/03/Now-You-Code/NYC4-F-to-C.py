'''
Now You Code 4: Fahrenheight to Celcius

Write a Python program to enter temperature in degrees Fahrenheight and convert
that temperature to degrees Celcius. 

For example:

    Enter temperature in deg F: 212
    That's 100.0 deg C

NOTES:
    - Research the converion formulas on your own.
    - Format output to one decimal place

Start out your program by writing your TODO list of steps
you'll need to solve the problem!
'''

# TODO: Write Todo list then beneath write your code
# Enter the temperature in degrees F:
# Enter formula
# Enter Print

far= int(input('Enter the temperature in Farenheit: '))
cel= ((far-32) * 5/9)
print("That's", '%.2f' % cel,'degrees celcius') 
