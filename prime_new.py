import math 
def chec(n): 
    if n == 1: 
        return False
    for x in range(2, (int)(math.sqrt(n))+1): 
        if n % x == 0: 
            return False 
    return True
n = input()
n=int(n)
if chec(n): 
    print("yes")  
else: 
    print("no") 
