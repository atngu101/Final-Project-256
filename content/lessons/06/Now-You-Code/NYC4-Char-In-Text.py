'''
Now You Code 4: Find a character in text

Description

Write a program to input a character, and then some text. It should then output
the number of times the character was found in the text.

Requirements:

#1 Write a function char_in_text which returns an int value as to
the count of that character in the text

Function: char_in_text
Arguments: char, text
Returns: count of char in text

#2 You're going to need a deterministic loop to iterate over each character in
the text. 

Example Run #1:

    Enter Character: e
    Enter Text: Mike Fudge
    The character 'e' appears 2 times in the text.
    
Example Run #2:

    Enter Character: x
    Enter Text: oakland
    The character 'x' appears 0 times in the text.
    
Start out your program by writing your TODO list of steps
you'll need to solve the problem!
'''

# TODO: Write Todo list then beneath write your code
# import string
# enter the input text (string)
# enter character (string)
# define and argue
# print the end

# Write code here 
char = str(input('Enter character: '))
text = str(input('Enter Text: '))
def char_in_text(char, text):
    count = str(text)
    character = str(text).count(char)
    return character

print('The character', char, 'appears', char_in_text(char, text), 'times in the text')
    
    
    
