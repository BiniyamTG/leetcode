class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for i in nums:
            if i in unique:
                return True
            unique.add(i)
        return False
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for i in nums:
            if i in unique:
                return True
            unique.add(i)
        return False
