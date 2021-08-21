class Solution:
    def uniquePaths(self, m: int, n: int, memo: dict = {}) -> int:
        # Note the original function did not have a "memo" parameter. This was
        # added to facilitate necessary memoization in the recursion

        # If we go "out of bounds," no legal moves can be made- return 0
        if m == 0 or n == 0:
            return 0

        # Base case: we've reached the bottom right. There's 1 unique path in a
        # 1x1 board, so we return 1 
        if m == 1 and n == 1:
            return 1
        
        if (m, n) in memo:
            return memo[(m, n)]
        elif (n, m) in memo:
            return memo[(n, m)]
        
        memo[(m, n)] = self.uniquePaths(m - 1, n, memo) + self.uniquePaths(m, n - 1, memo)
        return memo[(m, n)]
        