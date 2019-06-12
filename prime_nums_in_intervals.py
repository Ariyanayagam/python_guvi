b,t=map(int,input().split())
for l in range(b,t+1):
  u=0
  for j in range(1,t):
    if l%j==0:
      u+=1
  if u==2:
    print(l,end=" ")
