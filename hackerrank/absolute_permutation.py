#https://www.hackerrank.com/challenges/absolute-permutation/problem?isFullScreen=true

n = 5
k = 1

forced_values = set()
forced_pairs = [0] * n

def f(n,k):

    if k == 0:
        return [j for j in range(1,n+1)]

    for j in range(n, 0, -1):
        if j+k>n and j-k<1:
            return [-1]
        elif j+k>n and j-k>=1:
            if j-k not in forced_values:
                forced_values.add(j-k)
                forced_pairs[j-1]=j-k
            else:
                return [-1]
        elif j+k<=n and j-k<1:
            if j+k not in forced_values:
                forced_values.add(j+k)
                forced_pairs[j-1]=j+k
            else:
                return [-1]
        else:
            pass


    for j in range(1, n+1):
        if forced_pairs[j-1]==0:
            if j-k not in forced_values:
                forced_pairs[j-1] = j-k
                forced_values.add(j-k)
            elif j+k not in forced_values:
                forced_pairs[j-1] = j+k
                forced_values.add(j+k)
            else:
                return [-1]

    return forced_pairs

P = f(n,k)
print(P)
