class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        left = 0
        right = 0
        used = dict()

        while right < len(s):
            if s[right] in used.keys() and used[s[right]] >= left:
                left = used[s[right]] + 1
            else:
                answer = max(answer, right - left + 1)

            used[s[right]] = right
            right = right + 1

        return answer
