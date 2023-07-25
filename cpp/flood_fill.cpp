#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    void dfs(vector<vector<int>> &image, int r, int c, int orig, int color)
    {
        if (r < 0 || r >= image.size() || c < 0 || c >= image[0].size() || image[r][c] != orig)
        {
            return;
        }

        image[r][c] = color;
        int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
        for (int i = 0; i < 4; i++)
        {
            int nr = r + d[i][0], nc = c + d[i][1];
            dfs(image, nr, nc, orig, color);
        }
    }

    vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int color)
    {
        if (image[sr][sc] != color)
        {
            dfs(image, sr, sc, image[sr][sc], color);
        }
        return image;
    }
};