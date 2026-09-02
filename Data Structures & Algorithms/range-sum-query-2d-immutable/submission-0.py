from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        # dp[r][c] stores the sum of the submatrix from (0, 0) to (r - 1, c - 1)
        self.dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for r in range(m):
            for c in range(n):
                self.dp[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.dp[r][c + 1]
                    + self.dp[r + 1][c]
                    - self.dp[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.dp[row2 + 1][col2 + 1]
            - self.dp[row1][col2 + 1]
            - self.dp[row2 + 1][col1]
            + self.dp[row1][col1]
        )