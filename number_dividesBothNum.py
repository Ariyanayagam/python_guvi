 nx, k = list(map(int,input().split()))
for i in range(k,0,-1):
  if nx%i == 0 and k%i == 0:
    print(i)
    break
