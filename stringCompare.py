s12, s2 = raw_input().split()
c = 0
for i in range(len(s12)):
  if s12[i] != s2[i]:
    c += 1
if c == 1:
  print "yes"
else:
  print "no"
