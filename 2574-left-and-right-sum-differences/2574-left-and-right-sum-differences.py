class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        result = []
        current = 0
        for i in nums:
            current = current + i
            result.append(abs((current-i)-(total-current)))
        return result
        