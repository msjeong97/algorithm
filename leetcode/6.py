class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rowDict = {i: list() for i in range(1, numRows + 1)}

        i = 1
        isIncr = True

        for c in s:
            rowDict[i].append(c)

            if isIncr:
                i = i + 1
                if i >= numRows:
                    isIncr = False
            else:
                i = i - 1
                if i <= 1:
                    isIncr = True
        
        answerList = list()
        for i in range(1, numRows + 1):
            answerList.extend(rowDict[i])

        return ''.join(answerList)
