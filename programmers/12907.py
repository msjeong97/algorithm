def solution(n, money):
    arr = [0 for i in range(n+1)]
    arr[0] = 1
    
    money.sort()
    
    for i in money:
        for j in range(i, n + 1):
            arr[j] = arr[j] + arr[j - i]
    
    return arr[n] % 1000000007

print(solution(5, [1, 2, 5]))
