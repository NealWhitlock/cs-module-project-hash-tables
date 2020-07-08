# Your code here
# Dictionary for storing values
storage = {}

def expensive_seq(x, y, z):
    # # Your code here

    # # This should be done with recursion
    # # Establish base case where x <= 0
    if x <= 0:
        return y+z

    # Check if value of x is a key in the dictionary, return value if so
    elif (100000000000000*x+y+z) in storage:
        return storage[(100000000000000*x+y+z)]

    # Recurse function and save keys and values as you go
    else:
        n = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
        storage[(100000000000000*x+y+z)] = n
        return n

    # print(x)




if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
