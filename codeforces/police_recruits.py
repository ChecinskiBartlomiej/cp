#https://codeforces.com/problemset/problem/427/A

t = int(input())
X = list(map(int, input().split()))
p = 0
nt = 0
for k in range(t):
    if X[k] >= 0:
        p += X[k]
    else:
        if p > 0:
            p += X[k]
        else:
            nt += 1

print(nt)