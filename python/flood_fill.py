from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r_lim, c_lim, orig = len(image), len(image[0]), image[sr][sc]
        def dfs(r, c):
            if r < 0 or r >= r_lim or c < 0 or c >= c_lim or image[r][c] != orig:
                return
            image[r][c] = color
            for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                new_r, new_c = r + dx, c + dy
                dfs(new_r, new_c)
        if orig != color: #if it already has the new color, there is no need to call dfs
            dfs(sr, sc)
        return image