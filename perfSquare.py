lx, r = list(map(int,input().split()))

count = 0

for i in range(1x,101):

  if i*i >= lx and i*i <= r:

    count += 1

print(count)
