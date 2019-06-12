cch=raw_input()
vo=['a','e','i','o','u']
if cch in vo:
  print "Vowel"
else:
  if cch.isalpha:
    print "Consonant"
  else:
    print "invalid"
