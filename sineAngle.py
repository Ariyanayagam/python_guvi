import math 
dx=float(input())
m1=math.radians(dx)
n=math.sin(m1)
if(m1<1):
    print(round(n,1))
elif(m1>1):
    print(round(n))
