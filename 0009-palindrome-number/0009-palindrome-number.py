class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        copy=x
        var=0

        while copy:
            var=var*10+copy%10
            copy=copy//10
        if var==x:
            return True
        else: 
            return False





     
               


        