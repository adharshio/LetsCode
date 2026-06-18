from collections import Counter
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = {}
        n = len(grid)
        repeated = 0
        missing = -1
        visited = [0] * (n*n)
        visited.append(0)
        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                seen[val] = seen.get(val,0) + 1
                if seen[val] == 2:
                    repeated = val
                visited[val] = 1

        for k in range(1,n*n+1):
            if visited[k] != 1:
                missing = k

        return [repeated,missing]
