import time

start_time = time.time()

"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Apply f(x) to the values in q
after_f = {}

for num in q:
    after_f[num] = f(num)

"""
Simplifying the equation f(a) + f(b) = f(c) - f(d) yields:
4a + 6 + 4b + 6 = 4c + 6 - 4d - 6
   4a + 4b + 12 = 4c - 4d
      a + b + 3 = c - d
We don't even need to apply the function f(x) except to print out the results. 
We can just use the values in the domain.
"""

# Dictionaries for left and right sides of equation
left = {}
right = {}

# Calculate the sum of each pair combination on the left side
for val1 in q:
    for val2 in q:
        left[(val1, val2)] = val1 + val2 + 3
        # If the right side two values are not the same number (which would give 0)
        # and the first one is bigger (to keep the result positive), save that
        if (val1 != val2 and (val1 > val2)):
            right[(val1, val2)] = val1 - val2

# Invert the right side dictionary to easily access keys from right given value
inv_right = {v: k for k, v in right.items()}

# Check if the values in the left dict match any values in the right dict
# If so, get the key from the right dict by using the inverted dict
# Count how many permutations as well
perm = 0
for k, v in left.items():
    if v in right.values():
        #print(k, inv_right[v])
        print(f"f({k[0]}) + f({k[1]}) = f({inv_right[v][0]}) - f({inv_right[v][1]}) \
        {after_f[k[0]]} + {after_f[k[1]]} = {after_f[inv_right[v][0]]} - {after_f[inv_right[v][1]]} = {after_f[k[0]] + after_f[k[1]]}")
        perm += 1

print(perm, "different permutations found.")
print("--- %s seconds ---" % (time.time() - start_time))
