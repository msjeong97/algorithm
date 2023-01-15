def solution(n, times):
    min_time = min(times)
    low_answer = 1
    high_answer = min_time * n
    answer = high_answer
    
    while low_answer <= high_answer:
        mid_answer = int((low_answer + high_answer)/2)
        
        possible_count_in_mid_answer = 0
        for time in times:
            possible_count_in_mid_answer += int(mid_answer/time)
            
        if possible_count_in_mid_answer >= n:
            answer = min(answer, mid_answer)
            high_answer = mid_answer - 1
        else:
            low_answer = mid_answer + 1
            
    return answer

print(solution(6, [7, 10]))

