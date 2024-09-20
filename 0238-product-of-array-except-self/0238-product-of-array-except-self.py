class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        prefix = [1]
        for num in nums:
            prefix.append(prefix[-1] * num)
        suffix = [1]
        for num in reversed(nums):
            suffix.append(suffix[-1] * num)
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[-(i+2)])

        return result
                
            
        