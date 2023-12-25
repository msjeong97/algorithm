class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = list()
        result = list()

        def backtrack(open: int, close: int) -> None:
            if open == close == n:
                result.append(''.join(stack))
                return

            if open < n:
                stack.append('(')
                backtrack(open + 1, close)
                stack.pop()
            if close < open:
                stack.append(')')
                backtrack(open, close + 1)
                stack.pop()

            return
        
        backtrack(0, 0)

        return result   
