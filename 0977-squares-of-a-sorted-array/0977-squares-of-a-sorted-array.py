class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared=[]
        k=[abs(num) for num in nums]
        m=sorted(k)


        for i in m:
            k=i**2
            squared.append(k)
        return squared


        