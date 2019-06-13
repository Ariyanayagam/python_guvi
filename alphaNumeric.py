aaa1=input()
x=0
for i in range(0,len(aaa1)):
  if aaa1[i].isdigit():
    x=x+1
    break
for i in range(0,len(aaa1)):
  if aaa1[i].isalpha():
    x=x+1
    break
if x==2:
  print("Yes")
else:
  print("No")
