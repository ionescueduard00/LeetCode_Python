class Solution:
    def mySqrt(self, x: int) -> int:
        mid=0
        high=x
        low=0
        while low<=high:
            mid=(low+high)//2
            if mid*mid<=x:
                result=mid
                low=mid+1
            else:
                high=mid-1
        return result
                
           
        
        