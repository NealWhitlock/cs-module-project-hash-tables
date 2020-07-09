# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Read in text
with open("ciphertext.txt") as f:
    text = f.read()

# Dictionary to count occurances of letters
counts = {}

# Iterate through characters in text
# If the character is a letter incremement count in dictionary
for char in text:
    if char.isalpha() and char != 'â':
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1


# Organize results by most highest count
sorted_list = list(counts.items())
# sorted_list.sort(key=lambda pair: (-pair[1],pair[0]))
sorted_list.sort(key=lambda pair: -pair[1])

# for tup in sorted_list:
#     print(tup)

# print(len(sorted_list))

# String of alphabet ordered by frequency but doubled
freq = "ETAOHNRISDLWUGFBMYCPKVQJXZ"


# Dictionary to contain key for decoding
key = {}
for i, tup in enumerate(sorted_list):
    key[tup[0]] = freq[i]

# String to hold decrypted text
decoded = ""

# Reverse mapping to decode text
for char in text:
    if char.isalpha() and char != 'â':
        char = key[char]

    # print(char, end="")

    decoded += char


print(decoded)
