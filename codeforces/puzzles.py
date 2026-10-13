#https://codeforces.com/problemset/problem/337/A

n, m = map(int, input().split())
X = list(map(int, input().split()))

X.sort()

bn = 1001

M = bn
for j in range(m-n+1):
    d = X[j+n-1] - X[j]
    if d < M:
        M = d

print(M)


    


