def arm(numo):
  sum = 0
  temp = numo
  while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
  if numo == sum:
    print(numo)
num1,num2 = raw_input().split()
num1=int(num1)
num2=int(num2)
for i in range(num1,num2):
  arm(i)
