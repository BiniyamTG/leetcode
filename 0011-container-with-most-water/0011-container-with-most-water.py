class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        
        left = 0
        right = len(height) - 1
        
        # then by using while loop to itterate and find maximum area
        while left < right:
            area = 0
            
            area = (right - left) * min(height[right], height[left])
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
            result = max(area, result)
            
        
        return result
        