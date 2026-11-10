class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        maxim=0
        d=dict()
        while i<len(s):
            if s[i] in d:
                while s[i] in d:
                    del d[s[j]]
                    j+=1
            else:
                d[s[i]]=i
                i+=1
                if len(d)>maxim:
                    maxim=len(d)
        return maxim

            

        