h=input()
c=0
for i in h:
  if(i=='a' or i=='e' or i=='i' or i=='u' or i=='o'):
    print("yes")
    c=1
    break
if(c==0):
  print("no")
