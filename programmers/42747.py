def solution(citations):
    citations_sorted = sorted(citations, reverse=True)
    answer = 0
    
    for i in range(len(citations_sorted)):
        if citations_sorted[i] >= i + 1:
            print(i + 1)
            answer = max(i + 1, answer)
    
    return answer
