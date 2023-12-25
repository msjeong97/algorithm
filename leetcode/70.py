class Solution:
    def climbStairs(self, n: int) -> int:
        answer = list()
        answer.append(0)
        answer.append(1)
        answer.append(2)
        
        if n <= 2:
            return answer[n]
        else:
            for i in range(3, n + 1):
                answer.append(answer[i - 2] + answer[i - 1])

            return answer[n]
