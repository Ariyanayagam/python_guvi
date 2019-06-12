n = int(input())
sum = 0
t = n
while t > 0:
   digit = t % 10
   sum += digit ** 3
   t //= 10
if n == sum:
   print("yes")
else:
   print ("no")
