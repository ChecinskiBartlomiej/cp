#https://codeforces.com/problemset/problem/1418/A

t = int(input())

for j in range(t):
    x,y,k = map(int, input().split())
    print((k+k*y+x-3)//(x-1)+k)



