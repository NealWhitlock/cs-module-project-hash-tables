# Use regex to clean up non-alphanumeric characters
import re

def word_count(s):
    # Dictionary to store counts
    counts = {}

    # Lowercase everything and replace returns and tabs with spaces
    s = s.lower().replace('\n', ' ').replace('\t', ' ').replace('\r', ' ')

    # DON'T remove (because it might be escaping an apostrophe)
    keepers = "\ '"
    # Get rid of non-useful characters
    s = re.sub(r'[^\w'+keepers+']', '', s)

    # Split string on whitespace
    s = s.split()

    # Iterate over each word and either add to counts dictionary or increment
    for word in s:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    # Return counts dictionary
    return counts



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))