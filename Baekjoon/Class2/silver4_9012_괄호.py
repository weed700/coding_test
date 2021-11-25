#arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    PS = list(sys.stdin.readline().rstrip())
  
    s = []
    count = 0
    #첫 번째가 ")"괄호로 시작하면 무조건 잘 못된 경우
    if PS[0] == ")":
        print("NO")
    else:
        #스택에 괄호 넣고 빼기
        for i in range(len(PS)):
            if PS[i] == "(":
                s.append("(")
            else:
                if not s:
                    count += 1
                else:   
                    s.pop()
        
        #리스트 개수만큼 반복이 끝난 후 스택에 남아있는지 확인
        #스택에 남아있으면 VPS가 아님
        #단 리스트 중간에 스택이 비어있을 경우 count 변수로 체크
        #=>빈 스택에 ")" 괄호가 들어오는 잘 못된 경우
        if not s:
            if 0 != count:
                print("NO")
            else:
                print("YES")
        else:
            print("NO")
            
    
        