nx, k = list(map(int,input().split()))

f = 0

for i in range(nx):

  if k**i == nx:

    f = 1

    break

if f == 1:

  print("yes")

else:

  print("no")
