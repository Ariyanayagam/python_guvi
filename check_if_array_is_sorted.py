sx=int(input())

sx=[int(x) for x in input().split()]

s1=sorted(sx)

if(sx==s1):

    print("yes")

else:

    print("no")
