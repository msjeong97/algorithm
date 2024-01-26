visited = [[0 for i in range (102)] for j in range(102)]

def is_on_line(x, y, rectangle):
    for rec in rectangle:
        x1 = rec[0]
        y1 = rec[1]
        x2 = rec[2]
        y2 = rec[3]

        if x1 == x or x2 == x:
            if y >= y1 and y <= y2:
                return True
        elif y1 == y or y2 == y:
            if x >= x1 and x <= x2:
                return True

    return False

def is_possible_x_y(x, y, rectangle):
    if visited[x][y]:
        return False
    if x < 1 or x > 50:
        return False
    if y < 1 or y > 50:
        return False
            
    return is_on_line(x, y, rectangle)

def are_on_same_rectangle_line(x, y, x_, y_, rectangle):
    for rec in rectangle:
        x1 = rec[0]
        y1 = rec[1]
        x2 = rec[2]
        y2 = rec[3]
        
        if (x1 == x and x1 == x_) or (x2 == x and x2 == x_):
            if y >= y1 and y <= y2 and y_ >= y1 and y_ <= y2:
                return True
        elif (y1 == y and y1 == y_) or (y2 == y and y2 == y_):
            if x >= x1 and x <= x2 and x_ >= x1 and x_ <= x2:
                return True

    return False

def are_on_same_rectangle(x, y, x_, y_, rectangle):
    cnt = 0
    for rec in rectangle:
        x1 = rec[0]
        y1 = rec[1]
        x2 = rec[2]
        y2 = rec[3]
        
        if x1 <= x and x <= x2 and y1 <= y and y <= y2 and x1 <= x_ and x_ <= x2 and y1 <= y_ and y_ <= y2:
            cnt = cnt +1

    return cnt >= 2


def bfs(rectangle, characterX, characterY, itemX, itemY):
    queue = list()
    queue.append((characterX, characterY, 0))
    
    while queue:
        x, y, move = queue.pop(0)
        visited[x][y] = 1
        
        if (x, y) == (itemX, itemY):
            return move
        
        if is_possible_x_y(x + 1, y, rectangle) and are_on_same_rectangle_line(x, y, x + 1, y, rectangle) and not are_on_same_rectangle(x, y, x + 1, y, rectangle):
            queue.append((x + 1, y, move + 1))
        if is_possible_x_y(x - 1, y, rectangle) and are_on_same_rectangle_line(x, y, x - 1, y, rectangle) and not are_on_same_rectangle(x, y, x - 1, y, rectangle):
            queue.append((x - 1, y, move + 1))
        if is_possible_x_y(x, y + 1, rectangle) and are_on_same_rectangle_line(x, y, x, y + 1, rectangle) and not are_on_same_rectangle(x, y, x, y + 1, rectangle):
            queue.append((x, y + 1, move + 1))
        if is_possible_x_y(x, y - 1, rectangle) and are_on_same_rectangle_line(x, y, x, y - 1, rectangle) and not are_on_same_rectangle(x, y, x, y - 1, rectangle):
            queue.append((x, y - 1, move + 1))
        
    return -1

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = bfs(rectangle, characterX, characterY, itemX, itemY)
    return answer

