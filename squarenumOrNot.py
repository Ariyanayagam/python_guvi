import math
nn,m=map(int,input().split())
k=(nn*m)
q=int(math.sqrt(k))
if(k==q*q):
	print("yes")
else:
	print("no")
