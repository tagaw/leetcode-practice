// https://leetcode.com/problems/2-keys-keyboard/

#include <bits/stdc++.h>
using namespace std;
class Solution {
    /*
    Idea:
    The way to get exactly n characters in the minimum steps involves finding out
        the prime factorization of n. Every prime number n' characters takes a minimum of n' 
        steps to achieve (copy + (n'-1)*paste). Since every non-prime number can be broken 
        down into its factorized primes, then the minimum steps to make up these primes 
        is the minimum steps to make the original number n.
        
    
    Create a helper function (count_and_factor(x)) that recursively counts up the
        number of steps needed to get x characters. This is done by iterating through every
        number in the range [2,sqrt(x)] and seeing if x is evenly divisible by any number
        in the range. If it is, then we can recursively call the function on the divisor
        and quotient. However, if x is not evenly divisible by any number in the set range,
        then that means that x must be prime and as a result, returns x steps. 
        
    Note: if n is 1, then there are zero steps to take since there is already a character.
    */
public:
    int minSteps(int n) {
        if (n == 1) return 0;
        
        return count_and_factor(n);
        
    }
    
    int count_and_factor(int x) {
        for (int i = 2; i < (int)sqrt(x)+1; i++) {
            if (x % i == 0) {
                // recursive call
                return (count_and_factor(i) + count_and_factor(x/i));               
            } 
        }
        // prime number, returns x
        return x;
    }
};