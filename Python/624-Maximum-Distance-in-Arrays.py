# https://leetcode.com/problems/maximum-distance-in-arrays/
from typing import *

class Solution:
    """
    Idea:
    Greedily assume each new array contains the new lowest minimum and new highest maximum.
        Compare these values with the actual min/max values encountered previously.
        Update the actual min/max values along with the distance. If you actually did 
        encounter a new min/max, update the existing values.
        
    Handling the operations in this way prevents comparing two elements from the same array
        since the min/max value being compared is from all previous elements till that point.
    """
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minval = arrays[0][0]
        maxval = arrays[0][-1]
        dist = float('-inf')
        
        for i in range(1,len(arrays)):
            curr_min = arrays[i][0]
            curr_max = arrays[i][-1]
            
            curr_dist = max(curr_max-minval,maxval-curr_min)
            
            dist = max(dist,curr_dist)
            
            minval = min(minval,curr_min)
            maxval = max(maxval,curr_max)
        
        return dist
            