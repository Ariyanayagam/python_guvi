x=input()
for i in range(len(x)):
  if (i%2==0):
    print(x[i+1],end='')
  else:
    print(x[i-1],end='')
