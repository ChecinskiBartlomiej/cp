#https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true

def staircase(n):
    # Write your code here
    k = n-1
    for j in range(n):
        s = " " * k + "#" * (j+1)
        k -= 1
        print(s)
