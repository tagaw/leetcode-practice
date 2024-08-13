// https://leetcode.com/problems/number-of-islands/
#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int numIslands(vector<vector<char>> &grid)
    {
        int ct = 0;

        for (int i = 0; i < grid.size(); i++)
        {
            for (int j = 0; j < grid[0].size(); j++)
            {
                if (grid[i][j] == '1')
                {
                    ct++;
                    dfs(grid, i, j);
                }
            }
        }
        return ct;
    };

    void dfs(vector<vector<char>> &grid, int i, int j)
    {
        if (i < 0 or i >= grid.size() or j < 0 or j >= grid[0].size())
        {
            return;
        }

        if (grid[i][j] == '0')
        {
            return;
        }

        grid[i][j] = '0';

        dfs(grid, i + 1, j);
        dfs(grid, i, j + 1);
        dfs(grid, i - 1, j);
        dfs(grid, i, j - 1);

        return;
    }
};