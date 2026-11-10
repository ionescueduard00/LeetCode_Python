class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index=0
        for i in range (len(haystack)):
            if (needle[0]==haystack[i]):
                for j in range (len(needle)):
                    if i+j>=len(haystack):
                        break
                    
                    if needle[j]==haystack[i+j]:
                        index+=1
                    else:
                        break
                if index==len(needle):
                    return i
                index=0
        return -1

        
        