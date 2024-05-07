class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=sorted(nums1+nums2)
        if len(nums)%2==0:
            return (nums[len(nums)//2]+nums[(len(nums)//2)-1])/2
        else:
            return nums[len(nums)//2]
            