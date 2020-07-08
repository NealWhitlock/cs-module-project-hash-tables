import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Split words up
splits = words.split()

# Word dict to store each word and a list of the words that follow it
words_dict = {}

# Lists for start words and stop words
start_words = []
stop_words = []

# Iterate through each word in the split except for the last one (enumerate?)
for i, word in enumerate(splits):
    if i == (len(splits)-1):
        break
    # If the word is in the word dict append the next word to it's value list
    if word in words_dict:
        words_dict[word].append(splits[i+1])

    # Else, add the word to the dict with the next word in a list as the value
    else:
        words_dict[word] = [splits[i+1]]
    
    # Check for start word and stop word conditions and add to appropriate sets
    if word[0].isupper() or (word[0] == '"' and word[1].isupper()):
        start_words.append(word)
    if word[-1] in ".!?" or (word[-1] == '"' and word[-2] in ".!?"):
        stop_words.append(word)




# TODO: construct 5 random sentences
for i in range(5):
    keep_going = True
    # Pick a random start word.
    word = random.choice(start_words)
    print(word, end=" ")
    # While loop to make one sentence
    while keep_going:
        # Pick a random word from the list of values in the words_dict and print it out
        new_word = random.choice(words_dict[word])
        print(new_word, end=" ")

        # If the chosen word is in the stop words list, start a new sentence.
        if new_word in stop_words:
            print()
            keep_going = False
        
        # Save most recent word for next iteration
        word = new_word

"""
These two constructed sentences are worth saving somewhere for posterity:

I've held the book lying near the old cat, and two!
"Blew--me--up," panted out, quite clear that Alice went round the White Knight is the table, at once!
"""