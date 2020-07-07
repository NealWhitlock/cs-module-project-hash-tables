# Your code here
import math
import random
import time

storage = {0:1}
results_dict = {}


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Get value of x^y
    v_0 = x ** y

    if v_0 in results_dict:
        return results_dict[v_0]

    # Helper function to populate dictionary with factorial values
    def fact_func(n):
        fact = 1

        if n in storage:
            return storage[n]

        if ((n - (n % 100)) in storage):
            fact = (n - (n % 100))

        for i in range(fact, n+1):
            fact *= i
            if i % 100 == 0:
                storage[i] = fact 

        if n not in storage:
            storage[n] = fact
        
        return storage[n]
    
    # Get factorial of v
    v = fact_func(v_0)

    # Floor division
    v //= (x+y)

    # Modulo
    v %= 982451653

    results_dict[v_0] = v

    return v


start_time = time.time()
# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    # print(x,y)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')


print("--- %s seconds ---" % (time.time() - start_time))