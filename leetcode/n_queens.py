#https://leetcode.com/problems/n-queens/description/

n=8

def calculate_prohibited_from_j_k(j,k):
    to_add=set()
    l=1
    while j+l<n and k-l>=0:
        to_add.add((j+l,k-l))
        l+=1
    l=1
    while j+l<n:
        to_add.add((j+l,k))
        l+=1
    l=1
    while j+l<n and k+l<n:
        to_add.add((j+l,k+l))
        l+=1
    return to_add

result=[]
current=[]
def backtrack(j,prohibited):
    if len(current)==n:
        result.append(current.copy())
        return
    for k in range(n):
        if (j,k) in prohibited:
            continue
        s = "."*k+"Q"+"."*(n-k-1)
        current.append(s)
        to_add=calculate_prohibited_from_j_k(j,k)
        backtrack(j+1,prohibited|to_add)
        current.pop()

prohibited=set()
backtrack(0,prohibited)
print(result)
print(len(result))