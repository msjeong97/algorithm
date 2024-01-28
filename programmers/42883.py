def solution(number, k):
    stack = list()
    
    for num in number:
        if not stack:
            stack.append(num)
        else:
            if k == 0:
                stack.append(num)
            else:
                while k > 0 and stack:
                    if stack[-1] < num:
                        stack.pop()
                        k = k - 1
                    else:
                        break

                stack.append(num)

    return ''.join(stack[0:len(stack) - k])
