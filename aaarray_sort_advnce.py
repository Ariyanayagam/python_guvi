a=int(input())
a5=list(map(int,input().split()))
a5.sort()
for i in range(0,len(a5)):
  print(a5[i],end=' ')
