ii=input()
j,l="",""
for i in range(0,len(ii)):
  if(i%2==0):
    j+=ii[i]
  else:
    l+=ii[i]
print(j,l)
