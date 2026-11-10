class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i=len(digits)-1
        k=0
        while i>-1:
            if digits[i]==9:
                digits[i]=0
                k=1
            else :
                digits[i]+=1
                k=0
                break
            i-=1
        if k==1:
            return [1]+digits
        else:
            return digits
            

        
    





        