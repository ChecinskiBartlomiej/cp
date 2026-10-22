#https://codeforces.com/problemset/problem/1715/B

t=int(input())
for _ in range(t):
    n,k,b,s=map(int,input().split())
    if s<b*k or s>b*k+n*(k-1):
        print(-1)
    else:
        A=[0]*n
        A[0]=b*k
        r=s-b*k
        for j in range(n):
            x=min(r,k-1)
            A[j]+=x
            r-=x
        print(*A)

