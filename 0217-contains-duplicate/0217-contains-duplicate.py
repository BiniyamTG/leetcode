class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique=[]
        for i in nums:
            if i not in unique:
                unique.append(i)
        if len(unique)==len(nums):
            return False
        else:
            return True
        

     