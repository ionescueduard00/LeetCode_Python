class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
     seen={}
     result=0
     for i in range (len(nums)):
            result=target-nums[i]
            if result in seen:
                return (seen[result],i)
            seen[nums[i]]=i






    
        