class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s)
        k=0
        while i-1:
            if s[i-1]!=' ':
                break
            i-=1

        if i==0:
            return len(s)-1-k
    
        while i-1>-1:
            if s[i-1]!=' ':
                k+=1
            else:
                return k
            i-=1
        return k

        
        