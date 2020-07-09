import re

# Read in text from robin.txt
with open("robin.txt") as f:
    words = f.read()

# Clean text
# Make all lowercase
words = words.lower()

# Get rid of punctuation
words = re.sub(r'[^\w'+' '+']', '', words)

# print(words)

# Split the text up into individual words
words = words.split()

# Create dictionary for word counts and variable for longest word length
counts = {}
longest_word = 0

# Iterate through words and either add new ones or increment existing ones
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
        if len(word) > longest_word:
            longest_word = len(word)

# print(counts)

# Create sorted list of dictionary items by most common first
sorted_list = list(counts.items())
# sorted_list.sort(reverse=True, key=lambda pair: (pair[1],pair[0]))
sorted_list.sort(key=lambda pair: (-pair[1],pair[0]))

# sorted_list = sorted(counts, key=lambda x:(-x[1],x[0]))

# print(sorted_list)

for tup in sorted_list:
    print(tup[0].ljust(longest_word), "*"*tup[1])
# print(longest_word)
