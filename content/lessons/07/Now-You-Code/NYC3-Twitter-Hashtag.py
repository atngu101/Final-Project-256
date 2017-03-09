'''
Now You Code 3: Twitter Hashtag Detector

Let's write a program which extracts the twitter hashtags from the text.

Example Run 1:

    Enter Tweet: You got a 50 on the exam? #iamsad for you!
    Hashtag: #iamsad
    
Example Run 2:

    Enter Tweet: #lol too funny #joke #haha
    Hashtag: #lol
    Hashtag: #joke
    Hashtag: #haha

Example Run 3:

    Enter Tweet: Happy birthday @mafudge
    Hashtag: none

HINT: to handle the 3rd case you must keep a runnning count of hashtags
you find in the Tweet.


As usual, start out your program by writing your TODO list of steps
you'll need to solve the problem!
'''

# TODO: Write Todo list then beneath write your code
# Import string
# print Enter tweet
# split string
# define feature of hashtag
# print alternative statement with no hashtag (2 conditional statement)
    # 1 no hash
    # 2 with hashtag
# print hashtags


# Write code here
tweet = input('Enter tweet: ')
tokens = tweet.split(' ')
hashtag= '#'
count = 0
for token in tokens:
    if token[0] == hashtag:
        count = count + 1
        print('Hashtags:', token)
        continue
if count == 0:
    print('Hashtag: None')

            
