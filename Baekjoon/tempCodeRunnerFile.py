import sys

def solution(arr,start, end):
    stack = []
    
    for a in arr:
        if '.' == a:
            break   
        
        if not stack:
            if a in start:
                stack.append(a)
            if a in end:
                stack.append(a)
                return stack
        else:
            if a in start:
                stack.append(a)
            elif a in end:
                if start.get(stack[-1]) == end.get(a):
                    stack.pop()
                
    return stack


while True:
    arr = list(sys.stdin.readline().strip('\n'))

    start_check = {'(':0, '[':1}
    end_check = {')':0, ']':1}

    if '.' == arr[0]:
        break

    if not solution(arr,start_check, end_check):
        print('yes')
    else:
        print('no')