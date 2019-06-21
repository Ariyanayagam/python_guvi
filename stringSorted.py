lx=[]

m=int(input())

a=input().split()

for i in a:

  lx.append(i)

lx.sort()

lx.sort(key=len)

for i in lx:

  print (i,end=' ')
