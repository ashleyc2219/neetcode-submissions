class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        right = 0
        left = n - 1
        maxWater = 0
        # maxWater = height (max(heights[right], height[left] )) * length ( left - right )

        while(right < left):
            height = min(heights[right], heights[left])
            length = left - right
            maxWater = max(height*length, maxWater)
            if(heights[right] > heights[left]):
                left -= 1
            
            elif(heights[right] < heights[left]):
                right += 1
            
            else:
                left -= 1
                right += 1
            
        return maxWater
            

        