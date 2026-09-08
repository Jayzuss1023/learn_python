from typing import List
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0


        while left < right:
            # max area = length * width
            # The length is calculated by taking the distance between all indexes: right - left
            #             
            area = max(area, (right - left) * min(height[right], height[left]))
             
            # Incrementing or decrementing left or right side
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        print(area)
        return area


        

def main():
    solution = Solution()
    solution.maxArea([1,8,6,2,5,4,8,3,8])

main()