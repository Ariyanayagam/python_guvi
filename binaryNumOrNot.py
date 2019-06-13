strin=list(map(int,input()))
for i in range(len(strin)):
  if(strin[i]==0 or strin[i]==1):
    continue
  else:
    break
if(i==len(strin)-1):
  print("yes")
else:
  print("no")
