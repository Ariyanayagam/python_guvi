z=int(input())
ij=input()
ss=""
s=['a','e','i','o','u','A','E','I','O','U']
for k in ij:
    if k not in s:
        ss+=k
print(ss[::-1])
