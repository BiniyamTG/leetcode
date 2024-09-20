class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        counter=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        counter=counter+1
        return counter



