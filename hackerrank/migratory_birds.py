#https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true

def migratoryBirds(arr):
    # Write your code here
    d={}
    for j in range(len(arr)):
        if arr[j] not in d:
            d[arr[j]]=0
        d[arr[j]]+=1
    M=0
    iM=0
    for k in d:
        if d[k]>M:
            M=d[k]
            iM=k
        elif d[k]==M:
            if k<iM:
                iM=k
    return iM
