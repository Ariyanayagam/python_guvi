ss = int(raw_input())
if ss>1:
  for i in range(2,ss):
    if ss%i == 0:
      print "yes"
      break
  else:
    print "no"
else:
  print "yes"
