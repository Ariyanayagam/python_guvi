as = list(input())
s1=''
for i in range(0,len(as),2):
  t=as[i]
  as[i]=as[i+1]
  as[i+1]=t
  s1=s1+as[i]+as[i+1]
print(s1)
