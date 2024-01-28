def solution(people, limit):
    answer = 0
    people_sorted = sorted(people)
    left = 0
    right = len(people_sorted) - 1
    
    while left <= right:
        if people_sorted[left] + people_sorted[right] <= limit:
            left = left + 1
            right = right - 1
        else:
            right = right - 1
        
        answer = answer + 1

    return answer
