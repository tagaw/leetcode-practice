# https://leetcode.com/problems/kth-largest-element-in-a-stream/

import heapq
from typing import * 

class KthLargest:
    """
    Methodology:
    
    On init, create a minheap from the stream.
        If the size of the stream is less than k, add '-inf' (-10001) to act as a dummy head
        Otherwise, pop elements until the heap is k large. 
        The top of the heap will be the kth largest value
        
    On add, compare val to the top of the heap.
        If val is less or eq to top, do nothing return top.
        Otherwise push new val, pop old head, return new head.
    """
    def __init__(self, k: int, nums: List[int]):
        self.q = nums
        heapq.heapify(self.q)
        
        # shrink heap to k big
        while len(self.q) > k:
            heapq.heappop(self.q)
            
        # if stream is smaller than k, add dummy value.
        # next add is guarenteed to increase the heap to k large
        if len(self.q) < k:
            heapq.heappush(self.q,-10001)


    def add(self, val: int) -> int:
        # if the value is less than current kth largest, do nothing
        if val <= self.q[0]:
            return self.q[0]
        
        # push new value, pop old one to maintain k size heap
        heapq.heappush(self.q,val)
        heapq.heappop(self.q)
        
        return self.q[0]