#https://codeforces.com/problemset/problem/96/A

w = input()

l = 1
p = w[0]
d = 0

for b in w[1:]:
    if b == p:
        l += 1
    else:
        l = 1
        p = b
    if l == 7:
        d = 1
        print("YES")
        break

if d == 0:
    print("NO")