import math
from time import time

def iterate(x):
    x = str(x)
    b = x[:-1]
    e = int(b)
    f = 2 * int(x[-1:])
    ans = e - f
    return ans

t1 = time()

for a in range(1000000):
    x = a
    while len(str(x)) != 1:
        x = iterate(x)
        while x <= 0:
            x = x + 7
    if x == 7:
        if a % 7 != 0:
            print(f"false negative: {a}")
    elif a % 7 == 0:
        print(f"false positive: {a}")
        
t2 = time()

print(f"time taken: {t2-t1}")
