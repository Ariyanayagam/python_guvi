si=int(input())
a=""
for i in range(1,si+1):
	if si%i==0 and i%2==0:
		a=a+str(i)+" "
print(a.strip())
