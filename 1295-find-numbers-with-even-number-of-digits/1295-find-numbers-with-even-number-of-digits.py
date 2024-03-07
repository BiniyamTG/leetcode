class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            k=str(i)
            if (len(k)%2==0):
                count=count+1
        return count

        