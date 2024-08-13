# https://leetcode.com/problems/combination-sum-ii
from typing import *

class Solution:
    """
    Idea:
    Backtrack all possible combinations and add them to a list of valid combos if a 
    target amount is reached.
    
    Sort all numbers in candidates and recursively check if adding each number will
        contribute to a valid combo. While building combinations, skip identical elements 
        to prevent recalculating a previously seen combination. If adding a number exceeds the
        target amount, we can stop recursion and ignore current combination since no combo can
        exist on the travelled branch

    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        n = len(candidates)
        
        candidates.sort()
        
        def backtrace(amt,idx,combo):
            if amt < 0:
                return
            if amt == 0:
                answer.append(combo)
                return
            for i in range(idx,n):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue 
                backtrace(amt-candidates[i],i+1,combo+[candidates[i]])
        
        backtrace(target,0,[])
        return answer