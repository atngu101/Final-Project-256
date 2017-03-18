'''
Now You Code 4: Email Harvesting Training

Description

Write a program to extract the email addresses from the mailbox
file "NYC4-mbox-short.txt" and save them into another file
"NYC4-emails.txt" with one extracted email address per line.

The best way to find the emails in the mailbox file is to search
for lines in the file that begin with "From:". When you find an email
write just the address (not "From:" and the address) to
"NYC4-emails.txt", and don't worry about duplicates.

The program should print the number of emails it wrote to the file.

Example Run:

Wrote 27 emails to NYC4-emails.txt


Start out your program by writing your TODO list of steps
you'll need to solve the problem!
'''

# TODO: Write Todo list then beneath write your code
# link both files
# open file and read the lines
# open both files for data extraction
# if conditions fall write the text to the other text file.
# count =0 and add each time it writes an email to other file


# Write code here 
filename = "NYC4-emails.txt", "NYC4-mbox-short.txt"
count = 0
with open("NYC4-emails.txt") as f:
    with open("NYC4-mbox-short.txt", "w") as handle:
        for line in f:
            if "@" in line:
                handle.write(line)
                count += 1
print('Wrote', count, 'emails to NYC-mbox-short.txt')