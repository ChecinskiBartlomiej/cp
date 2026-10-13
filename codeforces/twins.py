#https://codeforces.com/problemset/problem/160/A

n = int(input())
A = list(map(int, input().split()))

#n = 4
#A = [2,1,2,2]

A.sort(reverse=True)
S = sum(A)
s = 0

for j in range(n):
    if 2 * s <= S:
        s += A[j]
    if 2 * s > S:
        print(j+1)
        break
