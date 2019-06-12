l,u=raw_input().split()
lowe=int(l)
uppe=int(u)
for num in range(lowe,uppe):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print num,
