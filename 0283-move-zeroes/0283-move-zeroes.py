class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        copy=0
        while i<len(nums) and j <len(nums):
            while i<len(nums) and nums[i]==0 :
                i+=1
            while j<len(nums) and nums[j]!=0 :
                j+=1
            if i<len(nums) and j<len(nums):
                if j<i:
                    copy=nums[i]
                    nums[i]=nums[j]
                    nums[j]=copy
                    i+=1
                    j+=1
                else:
                    i+=1
                
            
            
            
            
            

        