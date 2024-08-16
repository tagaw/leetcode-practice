# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import * 

class Solution:
    """
    Idea:
    Starting from the beginning of the array, create a window, keeping track of 
        all elements visited. Have a second pointer that tracks the start of that window
        and move the start up as much as you can before the total sum of elements within 
        the window drops below the target val, keeping track of the distance between the two
        pointers.
        
    The window will reach the end of the array without ever updating the start of the window
        if there is no subarray with a total value equal to the target.
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        dist = float('inf')
        j = 0
        val = 0
        for i in range(len(nums)):
            val += nums[i]
            
            while val >= target:
                val -= nums[j]
                dist = min(dist,i-j+1)
                j += 1
   
        return 0 if dist == float('inf') else dist
        