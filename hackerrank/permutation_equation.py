#https://www.hackerrank.com/challenges/permutation-equation/problem?isFullScreen=true

def permutationEquation(p):
    # Write your code here
    d={}
    for j in range(len(p)):
        d[p[j]]=j+1
    out=[]
    for j in range(1,len(p)+1):
        out.append(d[d[j]])
    return out