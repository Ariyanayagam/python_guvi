i,j=map(int,input().split())
i*=j
for r in range(1,1000):
  if((r*r)==i):
    print ("yes")
    j=0
if(j!=0):
  print("no")
