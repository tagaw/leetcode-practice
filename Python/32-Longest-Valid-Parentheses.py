# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    """
    Idea:
    Use a stack to track indices of opening parentheses
        Invalid parentheses will change the size of stack eventually.
        If the stack becomes empty, the longest substring till that point has been reached.
        Current index will become the start of a new possible substring.
    
    Longest possible substring is found by updating possible max length substring on 
        every successful matching parentheses using the stack.
        
    """
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1] # accounts for 0-index length
        mx = 0
        for i,p in enumerate(s):
            if p == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # longest substring to current pos found, start new search
                    stack.append(i)
                else:
                    # updates length when matching pair is made
                    mx = max(mx,i-stack[-1])
        return mx