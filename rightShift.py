sx = [int(x) for x in input().split()]
s1 = [int(x) for x in input().split()]
s2=''
for i in range(0,sx[1]):
  s1 = [s1[-1]] + s1[:-1]
print(*s1,sep=' ')
