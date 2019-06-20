i=int(input())
s=""
while(i>0):
    m=i%16
    if m<10:
        s=str(m)+s
    else:
        s=chr(64+m%9)+s
    i//=16
print(s)
