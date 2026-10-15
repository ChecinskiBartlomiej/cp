#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true

def breakingRecords(scores):
    # Write your code here
    n=len(scores)
    m=scores[0]
    lm=0
    M=scores[0]
    lM=0
    for j in range(1,n):
        if scores[j]>M:
            M=scores[j]
            lM+=1
        elif scores[j]<m:
            m=scores[j]
            lm+=1
    return (lM,lm)