def solution(m, n, puddles):
    arr = [[0 for j in range(n + 1)] for i in range(m + 1)]
        
    for puddle in puddles:
        arr[puddle[0]][puddle[1]] = 0
        
    for i in range(1, m + 1):
        if [i, 1] in puddles:
            break

        arr[i][1] = 1
    
    for j in range(1, n + 1):
        if [1, j] in puddles:
            break

        arr[1][j] = 1
        
    for i in range(2, m + 1):
        for j in range(2, n + 1):
            if [i, j] not in puddles:
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
                
    return arr[m][n] % 1000000007
