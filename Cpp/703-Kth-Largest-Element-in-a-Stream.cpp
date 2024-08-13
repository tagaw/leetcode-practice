// https://leetcode.com/problems/kth-largest-element-in-a-stream/

#include <bits/stdc++.h>
using namespace std;

class KthLargest {
    /*
    Methodology | 
    From init, create max heap from given stream, pop kth largest items
        into a separate min heap. 
        
    If there are less than k items at init, 
        add will require a kth item by constraint.
        Therefore we can add a 'dummy' value to the top of the min heap for the first add
    
    At every add, compare value to top of heap, 
        if less or eq, return top,
        if greater, insert value, pop first top and return new top.
    */
    
private:
    vector<int> heap; // heap of at most k items
    
public:
    KthLargest(int k, vector<int>& nums) {
        make_heap(nums.begin(),nums.end());
        int n = nums.size();
        for (int i = 0; i < k and i < n; i++) {
            heap.push_back(nums.front());
            
            pop_heap(nums.begin(),nums.end());
            nums.pop_back();  
        }
        
        // operator> as greater<int>() for min-heap
        make_heap(heap.begin(),heap.end(),greater<int>());
        
        // If there are < k items in heap, add kth item as '-inf' (-10001)
        if (heap.size() < k) {
            heap.push_back(-10001);
            push_heap(heap.begin(),heap.end(),greater<int>());
        }
    }
    
    int add(int val) {
        int top = heap.front();
        if (val <= top) {
            return  top;
        }
        
        // push val
        heap.push_back(val);
        push_heap(heap.begin(),heap.end(), greater<int>());
        
        // pop top return new top
        pop_heap(heap.begin(),heap.end(), greater<int>());
        heap.pop_back();
        
        return heap.front();
    }
};