from collections import defaultdict

# use defaultdict, not to check whether key is in dictionary
road_map = defaultdict(set)

def bfs_all(destination):
    # record all path_length from destination
    visited = dict()
    visited[destination] = 0
    queue = [destination]
    
    while queue:
        cur = queue.pop(0)
        for next in road_map[cur]:
            if next in visited:
                continue
            else:
                visited[next] = visited[cur] + 1
                queue.append(next)
    
    return visited
        

def solution(n, roads, sources, destination):
    for road in roads:
        loc1 = road[0]
        loc2 = road[1]
        
        road_map[loc1].add(loc2)
        road_map[loc2].add(loc1)
    
    minimum_path_length = bfs_all(destination)
    answer = [minimum_path_length.get(source, -1) for source in sources]

    return answer

