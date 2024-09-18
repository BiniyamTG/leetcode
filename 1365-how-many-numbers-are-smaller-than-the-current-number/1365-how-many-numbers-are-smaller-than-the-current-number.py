class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        counter=0
        for i in nums:
            for j in nums:
                if i>j:
                    counter+=1
            result.append(counter)
            counter=0

        return result
                
        