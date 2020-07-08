def no_dups(s):
    # Reference dictionary for words as they are encountered
    ref = {}

    # New string to return
    new_s = ""

    # Split the input string into words
    split = s.split()

    # Iterate through words in split string
    for word in split:
        # If word is not in reference dictionary add it to new string
        # with a space and put it in reference dictionary
        if word not in ref:
            new_s += word
            new_s += ' '
            ref[word] = 1
        # If the word is in the reference dictionary, don't add it
        else:
            continue
    
    # Return the new string, but stripped of outside whitespace
    return new_s.strip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))