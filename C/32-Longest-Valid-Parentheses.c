// https://leetcode.com/problems/longest-valid-parentheses/

int longestValidParentheses(char* s) {
    // Sloppy stack using static array and manual indexing
    int stack[30001];
    stack[0] = -1;
    int idx = 1;
    
    int max = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(') {
            stack[idx] = i;
            idx++;
        }
        else {
            idx--; // 'pop' from stack
            if (idx == 0) {
                stack[idx] = i;
                idx++;
            }
            else {
                max = (max > (i-stack[idx-1])) ? max : (i-stack[idx-1]);
            }
        }
    }
    
    return max;
}