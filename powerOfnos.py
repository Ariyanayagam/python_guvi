def pow(a,b):
    if(b==1):
        return a
    else:
        return a*pow(a,b-1)
i,j=map(int,input().split())
o=pow(i,j)
print(o)
