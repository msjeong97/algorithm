class Solution:
    def factorial(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            res = 1

            for i in range(1, n + 1):
                res = res * i

            return res

    def uniquePaths(self, m: int, n: int) -> int:
        return int(self.factorial(m - 1 + n - 1) / (self.factorial(m - 1) * self.factorial(n - 1)))
