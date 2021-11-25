#arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
import sys

T = int(sys.stdin.readline())

N = [int(sys.stdin.readline()) for _ in range(T)]

#다이나믹 프로그래밍(DP) : 큰 문제를 한 번에 해결하기 힘들 때 작은 여러 개의 문제로 나누어서 푸는 기법
#작은 문제들을 반복해서 푸는 경우를 제거하기 위함(매번 재계산 하지 않고 값을 저장해두었다가 재사용하는 방법)

zero = [1,0,1] #0~2일때 까지 호출되는 0의 개수 
one = [0,1,1]  #0~2일때 까지 호출되는 1의 개수

def fibonacci(num):
    l = len(zero)

    if l <= num:
        for i in range(l, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[num], one[num])

for n in N:
    fibonacci(n)

#################제귀함수 시간 초과#####################
# def fibonacci(num):
#     if 0 == num:
#         zero_count.append(0)
#         return 0
#     elif 1 == num:
#         one_count.append(1)
#         return 1
#     else:
#         return fibonacci(num-1)+fibonacci(num-2)

# for n in N:
#     zero_count, one_count = [], []

#     fibonacci(n)
#     print(len(zero_count), len(one_count))
    