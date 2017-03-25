'''
Now You Code 3: Sentiment 2.0

Let's improve on our basic sentiment analyzer in Python.

Copy the code from 1.0 most of it will be the same.

We will improve on this program by writing a user-defined
function load_words() to load the positve or negative words from a file.

For example, instead of:

pos = "happy glad joy"

we do this:

pos = load_words("NYC3-pos.txt")

We can now make the program "smarter" simply by adding positive and
negative words to the text files!


'''
filename = "NYC3-pos.txt", "NYC3-neg.txt"
# TODO: Write Todo list then beneath write your code
# Link the pos and neg .text
# define loadwords and link to the files
# execute the pre-loaded sentiment analyzer

# Write code here
def load_words(filename):
    with open(filename, 'r') as handle:
        return(handle.read().split(' '))
print('Sentiment analyzer')
    
while True:
    pos = load_words("NYC3-pos.txt")
    neg = load_words("NYC3-neg.txt")
    text = input('Enter Text or (type "quit" to stop): ').lower()
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

