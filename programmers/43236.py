def solution(distance, rocks, n):
    answer = 0
    left = 0
    right = distance
    rocks_sorted = sorted(rocks)
    rocks_sorted.append(distance)
    
    while left <= right:
        mid = (left + right) // 2
        
        rocks_removed = 0
        rock_prev = 0
        
        for rock in rocks_sorted:
            if rock - rock_prev < mid:
                rocks_removed = rocks_removed + 1
            else:
                rock_prev = rock
                
            if rocks_removed > n:
                break
        
        if rocks_removed > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
        
    return answer
