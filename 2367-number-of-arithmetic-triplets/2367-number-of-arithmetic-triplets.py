class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter=0
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                for k in range (j+1, len(nums)):
                    if (nums[j] - nums[i] == diff) and (nums[k] - nums[j] == diff):
                        counter=counter+1
        return counter

        