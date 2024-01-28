def solution(routes):
    answer = 0
    routes_sorted = sorted(routes, key=lambda x: x[1])
    latest_camera = -30001
    
    for route in routes_sorted:
        if route[0] > latest_camera:
            answer = answer + 1
            latest_camera = route[1]

    return answer
