'''
Now You Code 3: Sentiment 1.0

Let's write a basic sentiment analyzer in Python. Sentiment analysis is the
act of extracting mood from text. It has practical applications in analyzing
reactions in social media, product opinions, movie reviews and much more.

The 1.0 version of our sentiment analyzer will start with a string of
positive and negative words. For any input text and the sentiment score
will be calculated as follows:

for each word in our tokenized text
    if word in positive_text then
        increment seniment score
    else if word in negative_text then
        decrement sentiment score

So for example, if:
    positive_text = "happy glad like"
    negative_text = "angry mad hate"
    input_text = "Amazon makes me like so angry and mad"
    score = -1 [ +1 for like, -1 for angry, -1 for mad]

You want to write sentiment as a function:
Function: sentiment
Arguments: postive_text, negative_text, input_text
Returns: score (int)

Then write a main program that executes like this:

Sentiment Analyzer 1.0
Type 'quit' to exit.
Enter Text: i love a good book from amazon
2 positive.
Enter Text: i hate amazon their service makes me angry
-2 negative.
Enter Text: i love to hate amazon
0 neutral.
Enter Text: quit


NOTE: make up your own texts of positive and negative words.

Start out your program by writing your TODO list of steps
you'll need to solve the problem!
'''

# TODO: Write Todo list then beneath write your code
# import string 
# user enter string using like angry
# def 2 different types of emotions
# find a way to add up emotions based on score
# print in a neat fashion

# Write code here
while True:
    pos = ["happy", "like", "love", "glad"]
    neg = ["angry", "mad", "hate", "dislike", "sad"]
    text = input('Enter Text: ')
    if text == 'quit':
        break
        
    def senti(pos, neg, text):
        senti = 0
        tokens = text.split(' ')
        for word in tokens:
            if word in pos:
                senti = senti + 1
            elif word in neg:
                senti = senti - 1

        if senti > 0:
            print(senti, 'positive')
        elif senti < 0:
            print(senti, 'negative')
        elif senti == 0:
            print(senti, 'neutral')

    senti(pos, neg, text)

