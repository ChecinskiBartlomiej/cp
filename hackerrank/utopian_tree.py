#https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true

def utopianTree(n):
    # Write your code here
    h=1
    for j in range(n):
        if j%2==0:
            h*=2
        elif j%2==1:
            h+=1
    return h