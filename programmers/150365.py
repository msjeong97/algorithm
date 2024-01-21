def solution(n, m, x, y, r, c, k):
    def distance(x1, y1):
        return abs(r - x1) + abs(c - y1)
    
    def isImpossible(x1, y1, pathSum):
        return distance(x1, y1) > k - pathSum or (k - pathSum - distance(x1, y1)) % 2 == 1
    
    if isImpossible(x, y, 0):
        return 'impossible'
    
    stack = [(x, y, '')]
    
    while stack:
        i, j, path = stack.pop()
        pathSum = len(path)
        
        if i == r and j == c and pathSum == k:
            return path
        
        # d -> l -> r -> u
        if i > 1 and not isImpossible(i - 1, j, pathSum + 1):
            stack.append((i - 1, j, path + 'u'))
        if j < m and not isImpossible(i, j + 1, pathSum + 1):
            stack.append((i, j + 1, path + 'r'))
        if j > 1 and not isImpossible(i, j - 1, pathSum + 1):
            stack.append((i, j - 1, path + 'l'))
        if i < n and not isImpossible(i + 1, j, pathSum + 1):
            stack.append((i + 1, j, path + 'd'))

    return 'impossible'
