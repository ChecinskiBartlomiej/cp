#https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        vowels={"a","A","e","E","i","I","o","O","u","U"}
        j=0
        k=len(s)-1
        while j<k:
            while j<k and s[j] not in vowels:
                j+=1
            while j<k and s[k] not in vowels:
                k-=1
            if j<k:
                s[j],s[k]=s[k],s[j]
                j+=1
                k-=1
        s="".join(s)
        return s