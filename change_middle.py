ss=list(input())
if len(ss)%2==0:
    ss[int(len(ss)/2)] ='*'
    ss[int(len(ss)/2)-1]='*'
else:
    ss[int(len(ss)/2)] ='*'
for i in range(0,len(ss)):
    print(ss[i],end='')
