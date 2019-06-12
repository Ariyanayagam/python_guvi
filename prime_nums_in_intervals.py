l,u=map(int,input().split())
for num in range(l,u):
   if num > 1:
       for i in range(2,num/2):
           if (num % i) == 0:
               break
       else:
           print num,
