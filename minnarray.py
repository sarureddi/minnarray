number,k1=map(int,input().split())
lis=list(map(int,input().split()))
for i1 in range(k1):
    u1,v1=map(int,input().split())
    c1=lis[u1-1:v1]
    print(min(c1))
