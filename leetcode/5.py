class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        answer = ""

        def getPalindorme(left: int, right: int) -> str:
            while left - 1 >= 0 and right + 1 < n and s[left - 1] == s[right + 1]:
                left = left - 1
                right = right + 1

            return left, right
        
        for i in range(n):
            l1, r1 = getPalindorme(i, i)
            if (r1 - l1 + 1) > len(answer):
                answer = s[l1: r1 + 1]
            
            if i < n - 1 and s[i] == s[i + 1]:
                l2, r2 = getPalindorme(i, i + 1)
                if (r2 - l2 + 1) > len(answer):
                    answer = s[l2: r2 + 1]

        return answer
