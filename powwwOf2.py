xn = int(input())

f = 0

for i in range(1000):

  if i*i == xn:

    f = 1

    break

if f == 1:

  print("yes")

else:

  print("no")
