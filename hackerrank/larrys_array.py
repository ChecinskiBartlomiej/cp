#https://www.hackerrank.com/challenges/larrys-array/problem?isFullScreen=true

def larrysArray(A):
    # Write your code here
    inv = 0
    for j in range(len(A)):
        for k in range(j+1, len(A)):
            if A[j] > A[k]:
                inv += 1
    if inv % 2 == 0:
        return "YES"
    else:
        return "NO"