#https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true


S = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
n = len(S)
k = 7


remainders = [0] * k
for j in range(n):
    remainders[S[j] % k] += 1

out = 0

for j in range(k // 2 + 1):
    if j == 0:
        out += min(1, remainders[j])
    elif (k % 2 == 0) and (j == k // 2):
        out += min(1, remainders[j])
    else:
        out += max(remainders[j], remainders[k-j])
    
print(out)