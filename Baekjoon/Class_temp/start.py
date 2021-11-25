#arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
#from collections import Counter


import sys

def solution(arr,start, end):
    stack = []

    #리스트를 한글자씩 뽑아내어 비교    
    for a in arr:
        if '.' == a:
            break   
        
        #맨처음 스택이 비어있을 때
        if not stack:
            #처음 들어온 값이 start 괄호일 때
            if a in start:
                stack.append(a)
            #처음 들어온 값이 end 괄호이면 불균형으로 stack을 채워 리턴
            if a in end:
                stack.append(a)
                return stack
        #스택이 있을 경우(start 괄호들이 있을 경우)
        else:
            #들어온 a 값이 start 괄호이면 stack에 저장
            if a in start:
                stack.append(a)
            #들어온 a 값이 end 괄호이면 맨 위에 stack 값과 비교하여 맞으면 stack에서 pop
            elif a in end:
                if start.get(stack[-1]) == end.get(a):
                    stack.pop()
                else:
                    return stack
                
    return stack


while True:
    #문자열을 리스트로 만듬
    arr = list(sys.stdin.readline().strip('\n'))

    #딕셔너리로 괄호에 번호를 줌
    start_check = {'(':0, '[':1}
    end_check = {')':0, ']':1}

    # '.'이 들어오면 종료
    if '.' == arr[0]:
        break

    if not solution(arr,start_check, end_check):
        print('yes')
    else:
        print('no')