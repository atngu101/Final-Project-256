'''
Now You Code 3: Final Grade in IST256

Our Course Syllabus has a grading scale here:

http://ist256.syr.edu/syllabus/#grading-scale

Write a Python program to input a number of points earned out of 600 and then
outpus the registrar grade. After you get it working initially, re-write it
to handle bad input. 

For example:

    IST256 Grade Calculator
    Enter total points out of 600:  550
    Grade: A- 

Start out your program by writing your TODO list of steps
you'll need to solve the problem!
'''

# TODO: List 

#1. input grade out of 600 points
#2. lookup letter grade (use an if else ladder for lower bound of each grade)
#3. print letter grade.

# TODO Write code here
print('IST Grade Calculator')
try:
    you = int(input('Enter total points out of 600: '))
    if (you >= 570 or you == 600):
        print("Grade: A")
    elif (you >= 541 or you == 570):
        print('Grade: -A')
    elif (you >= 510 or you == 539):
        print('Grade: B+')
    elif (you >= 480 or you == 509):
        print('Grade: B')
    elif (you >= 450 or you == 479):
        print('Grade: B-')
    elif (you >= 420 or you == 449):
        print('Grade: C+') 
    elif (you >= 390 or you == 419):
        print('Grade: C')
    elif (you >=360 or you == 389):
        print('Grade: C-')
    elif (you >= 300 or you == 359):
        print('Grade: D')
    elif (you >= 0 or you == 299):
        print('Grade: F')
    else:
        print('You cannot have a grade less than 0 points!')       

except:
    print('That is not a grade!')
