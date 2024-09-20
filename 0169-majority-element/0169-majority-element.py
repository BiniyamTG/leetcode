class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element=0
        count = 0

        for i in nums:
            if count == 0:
                element = i
            count += (1 if i == element else -1)
            
        return element

       

            


        