class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        j=0
        result=""
        while j<len(strs[0]):
            for i in range (len(strs)):
                if j<len(strs[i]):
                    if strs[0][j]!=strs[i][j]:
                            return result
                else:
                    return result
            result+=strs[0][j]
            j+=1
        return result
                
                

        
       

        
                    




            
                
                
        