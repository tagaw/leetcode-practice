// https://leetcode.com/problems/minimum-size-subarray-sum/
#include <bits/stdc++.h>

using namespace std;

class Solution {
    /*
    Idea:
    Starting from the beginning of the array, create a window, keeping track of 
        all elements visited. Have a second pointer that tracks the start of that window
        and move the start up as much as you can before the total sum of elements within 
        the window drops below the target val, keeping track of the distance between the two
        pointers.
        
    The window will reach the end of the array without ever updating the start of the window
        if there is no subarray with a total value equal to the target.
    */
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int val = 0;
        
        // max length of nums is 100000
        int dist = 100001;
        int start = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            val += nums[i];
            
            while (val >= target) {
                val -= nums[start];
                dist = min(dist, i-start+1);
                start++;
            }
        }
        
        return (dist > 100000) ? 0 : dist;  
    }
};
