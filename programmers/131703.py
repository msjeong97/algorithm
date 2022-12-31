# https://school.programmers.co.kr/learn/courses/30/lessons/131703
def flip_row(row):
    for idx in range(len(row)):
        row[idx] = (row[idx] + 1) % 2


def check_row_can_be_a_target(row, row_target):
    if row == row_target:
        return True, 0
    else:
        flipped_row = [(i + 1) % 2 for i in row]
        if flipped_row == row_target:
            return

def check_arr_can_be_a_target(arr, target):
    more_flip_count = 0
    can_be_a_target = True

    for col_idx in range(len(arr[0])):
        col = [arr[i][col_idx] for i in range(len(arr))]
        col_target = [target[i][col_idx] for i in range(len(target))]

        if col == col_target:
            continue
        else:
            flipped_col = [(i + 1) % 2 for i in col]
            if flipped_col == col_target:
                more_flip_count += 1
            else:
                can_be_a_target = False
                break

    return can_be_a_target, more_flip_count


def search(row_idx, arr, target, cnt):
    # check arr can be a target
    can_be_a_target, more_flip_count = check_arr_can_be_a_target(arr, target)
    if can_be_a_target:
        return cnt + more_flip_count

    # if arr cannot be a target, check there is more way to search
    if row_idx >= len(arr):
        return -1

    # if there is more way to search, search
    flip_row(arr[row_idx])
    result_flip = search(row_idx + 1, arr, target, cnt + 1)
    flip_row(arr[row_idx])
    result_not_flip = search(row_idx + 1, arr, target, cnt)

    if result_flip > 0:
        if result_not_flip > 0:
            return min(result_flip, result_not_flip)
        else:
            return result_flip
    else:
        return result_not_flip


def solution(beginning, target):
    answer = search(0, beginning, target, 0)

    return answer


if __name__ == '__main__':
    beginning = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
    target = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
    print(solution(beginning, target))
