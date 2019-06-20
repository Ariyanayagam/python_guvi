t1x=list(map(int,input().split()))
for i in range(1,(t1x[0]*t1x[1])+1):
    if(i%t1x[0]==0 and i%t1x[1]==0):
        print(i)
        break
