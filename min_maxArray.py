i=list(map(int,input().split()))
mn=i[0]
mx=i[0]
for k in range(0,len(i)):
  if(i[k]>mx):
    mx=i[k]
  else:
    mn=i[k]
print(mx,mn)
