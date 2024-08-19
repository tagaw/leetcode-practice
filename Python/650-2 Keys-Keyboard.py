# https://leetcode.com/problems/2-keys-keyboard
from typing import *
import math

class Solution:
    """
    Idea: (originally done in c++)
    A number n can be reached in as many steps as the sum of its
        prime factorization and a prime number n' requires a minimum of
        n' steps. We can break n down into its prime factorization and 
        sum the values together to get a minimum number of steps to reach n.
    
    Firstly, check if n is 1, if it is, there are no steps needed. Otherwise
        we can recursively count the steps by breaking down n into a prime
        factor tree. To do this, for ever call to minSteps(n) we check if 
        n is divisible by any number in the range [2,sqrt(n)]. If it is, then
        then we recursively call minSteps on the divisor of n and the resulting
        quotient. The tree traversal will end with the base case of a number
        reaching all of its prime factors.
    """
    def minSteps(self, n: int) -> int:
        if n == 1: return 0
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return self.minSteps(i) + self.minSteps(n//i)
        return n