#https://codeforces.com/problemset/problem/318/A

n, k = map(int, input().split())


if n % 2 == 0:
    if k <= n / 2:
        print(2 * k - 1)
    else:
        print(2 * k - n)
else:  
    if k <= (n + 1) / 2:
        print(2 * k - 1)
    else:
        print(2 * k - n - 1)

