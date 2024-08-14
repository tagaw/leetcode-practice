# https://leetcode.com/problems/find-k-th-smallest-pair-distance/

from typing import *

class Solution:
    """
    Idea: 
    Perform a binary search over the range of possible distances after sorting,
        calculating the number of combinations that can be made within the 
        search distance; Updating the binary search based on the number of 
        combinations found.
        
    Sort the nums array to make calculating total combinations possible with a 
        sliding window. Initalize the binary search range as [0,MAX_DISTANCE] where 
        MAX_DISTANCE is the largest distance between two elements (max-min). Perform
        a binary search over the range, the value of the search is the kth distance.
        
    To count the combinations used for the binary search, create a sliding window in the
        sorted array to find the number of possible combinations within a specified distance. 
        The counts are calculated by adding up the distance between the elements in the sorted array.
        
    ALTERNATIVELY | set up a value:count hashmap and perform the sliding window over that
        data structure instead of using the nums array. Does not require sorting the nums array,
        only the unique values in nums.
    """
    def smallestDistancePair(self, nums: List[int], k: int) -> int:        
        nums.sort()
        
        low = 0 
        hi = nums[-1]-nums[0]
        
        def ct(dist):
            ct = 0
            l = 0
            
            # tallys up number of combinations within 'dist' in nums
            for r in range(len(nums)):
                while nums[r] - nums[l] > dist:
                    l += 1
                
                ct += r-l # summation
                
            return ct
                    
        # binary search
        while low < hi:
            mid = (low+hi)//2
            
            curr_ct = ct(mid)
            
            if curr_ct < k:
                low = mid+1
            else:
                hi = mid
                
        return low
        
        
    
        