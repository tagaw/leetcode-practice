#https://leetcode.com/problems/gas-station/

from typing import *

class Solution:
    """
    Idea:
    The total amount of gas you gain on the trip must be greater or equal to the total 
        amt of gas you use. If at any point your tank dips below 0, any stop before
        that point cannot be the starting index. Since there is guarenteed a unique
        answer, the first point from where the tank never reaches negative will be the 
        final return value.
        
    Firstly, create a total value to store the entire net gas gained over the entire trip,
        at the end, if this value is < 0 then there is no start. 
    
    Next, crate a value for the start and current tank and set them to 0. We can iterate over all 
        indices of the arrays and add the net gas gained at each point to both the total and
        tank. If the tank ever dips below 0, we assume the next position will be a valid start
        and reset the current trip's tank to 0. This is an assumption that uses the fact that there
        is a single unique solution. By making this assumption, the function chooses any non-negative
        net gas gain as a potential starting point and validates it as it goes through the array.
        
    Finally, during return, we check to see if the trip is even possible through the total value of
        gas gained through all points. If it is negative, then the trip is not possible and we return
        -1. Otherwise, we return the starting point that was chosen and then validated through 
        iterating the array.
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        total = 0
        tank = 0
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            
            tank += diff
            if tank < 0:
                start = i+1
                tank = 0
                
        return -1 if total < 0 else start
            
            