// https://leetcode.com/problems/lemonade-change/

#include <bits/stdc++.h>
using namespace std;


class Solution {
    /*
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
    */
public:
    bool lemonadeChange(vector<int>& bills) {
        int five = 0;
        int ten = 0;
        
        for (int& bill : bills) {
            if (bill == 5) {
                // case 1: No change, increase $5 bills on hand
                five++;
            }
            else if (bill == 10) {
                // case 2: Need 1 $5 bill to make change.
                if (five) {
                    five--;
                    ten++;
                }
                else return false;
            }
            else {
                // case 3: Need either 1 $5 and 1 $10 OR 3 $5
                if (five and ten) {
                    // Prioritize using 10's since this is their only use
                    five--;
                    ten--;
                }
                else if (five > 2) {
                    five -= 3;
                }
                else return false;
            }
        }
        return true;
    }
};