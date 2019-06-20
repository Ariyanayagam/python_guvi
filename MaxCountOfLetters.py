Px=input()
Q=Px[0]
for i in Px:
  if (Px.count(Q)<=Px.count(i)):
    Q=i
print(Q)
