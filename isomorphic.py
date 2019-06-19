s11, s2 = raw_input().split()
count = 0
for i in range(len(s1)):
  if s11.count(s1[i]) == s2.count(s2[i]):
    count += 1
if count == len(s11):
  print "yes"
else:
  print "no"
