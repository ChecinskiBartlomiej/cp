#https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true

def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    def my_binary_search(L,x):
        left=0
        right=len(L)-1
        ans=-1
        while left<=right:
            mid=(left+right)//2
            if L[mid]<=x:
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans
    
    drives=sorted(drives)
    M=-1
    for j in range(len(keyboards)):
        t=b-keyboards[j]
        d=my_binary_search(drives,t)
        if d!=-1:
            M=max(M,drives[d]+keyboards[j])
    return M