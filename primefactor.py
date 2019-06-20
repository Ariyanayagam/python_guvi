sx=int(input())
for z in range(2,sx+1):
  if(sx%z==0):
      t=0
      for i in range(2,z+1):
          if(z%i==0) and (i!=z):
              t=1
              break
      if(t==0):
          print(z,end=' ')
