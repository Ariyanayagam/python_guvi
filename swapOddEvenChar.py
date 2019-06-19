xa=input()
for i in range(len(xa)):
  if (i%2==0):
    print(xa[i+1],end='')
  else:
    print(xa[i-1],end='')
