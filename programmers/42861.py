def solution(n, costs):
    answer = 0
    costs_sorted = sorted(costs, key=lambda x: x[2])
    nodes = set()
    nodes.add(0)
    
    while len(nodes) < n:
        for cost in costs_sorted:
            if cost[0] in nodes and cost[1] in nodes:
                continue
            else:
                if cost[0] in nodes:
                    nodes.add(cost[1])
                    answer = answer + cost[2]
                    break
                elif cost[1] in nodes:
                    nodes.add(cost[0])
                    answer = answer + cost[2]
                    break
                
    return answer
