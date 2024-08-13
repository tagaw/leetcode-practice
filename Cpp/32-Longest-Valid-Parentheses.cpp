// https://leetcode.com/problems/longest-valid-parentheses/submissions/
#include <bits/stdc++.h>

using namespace std;

class Solution {
    /*
    Idea:
    Use a stack to track indices of opening parentheses
        Invalid parentheses will change the size of stack eventually.
        If the stack becomes empty, the longest substring till that point has been reached.
        Current index will become the start of a new possible substring.
    
    Longest possible substring is found by updating possible max length substring on 
        every successful matching parentheses using the stack.
    */
public:
    int longestValidParentheses(string s) {
        vector<int> stack = {-1};
        int longest = 0;
        
        for (int i = 0; i < s.size(); i++) {         
            if (s[i] == '(') {
                stack.push_back(i);
            }           
            else {
                stack.pop_back();
                
                if (stack.empty()) 
                    stack.push_back(i);
                
                else
                    longest = max(longest, i - stack.back());         
            }
        }
        
        return longest; 
    }
};
