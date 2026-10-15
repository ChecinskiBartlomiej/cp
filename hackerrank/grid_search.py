#https://www.hackerrank.com/challenges/the-grid-search/problem?isFullScreen=true

def gridSearch(G, P):
    # Write your code here
    def find_substring_in_string(s,t):
        n=len(s)
        m=len(t)
        beginnings=[]
        for j in range(n):
            k=0
            if s[j]==t[0]:
                b=j
                while k<m and j+k<n and s[j+k]==t[k]:
                    k+=1
                if k==m:
                    beginnings.append(b)
        return beginnings

    first = P[0]
    for j in range(len(G)-len(P)+1):
        beginnings=find_substring_in_string(G[j],first)
        if len(beginnings)>0:
            for b in beginnings:
                for m in range(1,len(P)):
                    if G[j+m][b:b+len(first)]!=P[m]:
                        break
                    if m==len(P)-1:
                        return "YES"
    return "NO"

