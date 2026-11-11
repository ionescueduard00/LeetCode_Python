class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy=0
        w=0
        for r in range (len(nums)):
            if r!=w and nums[r]!=0:
                copy=nums[r]
                nums[r]=nums[w]
                nums[w]=copy
            if nums[w]!=0:
                w+=1

                
            
            
            
            
            

        