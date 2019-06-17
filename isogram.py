m11=input()
m2=""
for i in m11:
  if i not in m2:
    m2=m2+i
if(m11==m2):
  print("Yes")
else:
  print("No")
