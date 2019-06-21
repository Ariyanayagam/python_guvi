s1x, s2, k = list(map(str,input().split()))

k = int(k)

count = 0

for i in range(len(s1x)):

  if s1x[i] != s2[i]:

    count += 1

if count == k:

  print("yes")

else:

  print("no")
