'''
Now You Code 3: Distance Conversions

Write a Python program to enter a distnace in feet then convert that
distance to yards and miles. 

For example:

    Enter distance in FEET:15000
    That's 5000.0 yards or 2.8 miles

NOTES:
    - Research the converion formulas on your own.
    - Format output to one decimal place

Start out your program by writing your TODO list of steps
you'll need to solve the problem!
'''

# TODO: Write Todo list then beneath write your code
# Enter Distance in Feet
# Enter the formula for yards and miles
# Convert to yards and miles

feet= int(input('Enter Distance in Feet: '))
yard= (feet/3)
miles =(feet/5280)
print("That's,", '%.2f' % yard, 'yards', 'or', '%.2f' % miles, 'miles')
          

