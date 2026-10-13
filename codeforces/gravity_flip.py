#https://codeforces.com/problemset/problem/405/A

n = int(input())
X = list(map(int, input().split()))

X.sort()

for x in X:
    print(x)