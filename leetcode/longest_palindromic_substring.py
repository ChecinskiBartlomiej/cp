#https://leetcode.com/problems/longest-palindromic-substring/

def longestPalindrome(s: str) -> str:

    n=len(s)
    M=1
    sM=0
    eM=0

    if n==1:
        return s[0]
    else:
        if s[0]==s[1]:
            M=2
            sM=0
            eM=1

        for j in range(1, n-1):

            k=0
            m=0

            while (j-1-k>=0) and (j+1+k<=n-1) and (s[j-1-k]==s[j+1+k]):
                k+=1
            
            while (j-m>=0) and (j+1+m<=n-1) and (s[j-m]==s[j+1+m]):
                m+=1

            if 1+2*k>=2*m:
                if 1+2*k>M:
                    sM=j-k
                    eM=j+k
                    M=1+2*k
            else:
                if 2*m>M:
                    sM=j-m+1
                    eM=j+m
                    M=2*m
        
        return s[sM:eM+1]

s = "babadda"

print(longestPalindrome(s))