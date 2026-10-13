#https://codeforces.com/problemset/problem/151/A

X = list(map(int, input().split()))

a = (X[1] * X[2]) // X[6]
b = X[3] * X[4]
c = X[5] // X[7]

d = (min(a, b, c)) // X[0]

print(d)



