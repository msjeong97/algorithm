class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)

        for i in range(0, int(n / 2) + 1):
            if s[i] == s[n - 1 - i]:
                continue
            else:
                return False
        
        return True
