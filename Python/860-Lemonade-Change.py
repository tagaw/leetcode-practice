# https://leetcode.com/problems/lemonade-change/
from typing import *

class Solution:
    """
    Idea:
    Recognize that change for a specific bill requires a minimum number of bills 
        to complete. a $5 requires nothing and leaves you a $5 bill for future change.
        $10 requires 1 $5 bill to make change and leaves you a $10 bill. A $20 bill
        requires 1 $10 bill and 1 $5 bill to make change OR 3 $5 bills.
        If at any point we don't have the required bills to make the transaction, we 
        return False.
        
    Iterate through all the bills tallying up the total amt of bills you have after each
        transaction. If there is an insufficient amt required for you to accept the bill
        return False. Return True if you iterate through the entire array.
    """
    def lemonadeChange(self, bills: List[int]) -> bool:        
        change = [0,0]
        
        for bill in bills:          
            match bill:
                case 5:
                    change[0] += 1             
                
                case 10:
                # case 2: $10 bill, make change and save $10 for later change                
                    if change[0]:
                        change[0] -= 1
                        change[1] += 1
                    else:
                        return False             
                
                case 20:
                # case 3: $20 bill, try making change 1 of 2 ways
                    if change[1] and change[0]:
                        # case 3.1: $10 and $5 change
                        change[0] -= 1
                        change[1] -= 1                            
                    elif change[0] > 2:
                        # case 3.2: 3x $5 change
                        change[0] -= 3
                    else:
                        return False
            
        return True