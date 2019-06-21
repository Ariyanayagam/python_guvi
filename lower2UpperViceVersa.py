sx = input()

s1 = ""

for i in range(len(sx)):

  if sx[i].isupper():

    s1 += sx[i].lower()

  elif sx[i].islower():

    s1 += sx[i].upper()

print(s1)
