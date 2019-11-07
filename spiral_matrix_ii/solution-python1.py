from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(0)
            result.append(row)

        counter = 1

        for depth in range(n // 2 + n % 2):
            for i in range(n - 2 * depth):
                result[depth][depth + i] = counter
                counter += 1
            for i in range(n - 1 - 2 * depth):
                result[depth + 1 + i][n - 1 - depth] = counter
                counter += 1
            for i in range(n - 1 - 2 * depth):
                result[n - 1 - depth][n - 2 - depth - i] = counter
                counter += 1
            for i in range(n - 2 - 2 * depth):
                result[n - 2 - depth - i][depth] = counter
                counter += 1
        return result
