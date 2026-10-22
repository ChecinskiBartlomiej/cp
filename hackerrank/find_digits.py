#https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true

def findDigits(n):
    # Write your code here
    s=str(n)
    count=0
    for j in range(len(s)):
        if s[j]=="0":
            continue
        if n%int(s[j])==0:
            count+=1
    return count