# 골드바흐의 추측 https://www.acmicpc.net/problem/6588

"""
'4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다'를 검증하시오
- n = a + b 형태로 출력
  -> 방법이 여러가지면 b - a가 가장 큰 것 출력
- 두 홀수 소수의 합으로 나타낼 수 없을 경우 'Goldbach's conjecture is wrong." 출력
"""
MAX_NUM = 10 ** 6

def get_prime_nums(n):
    is_prime_num = [True for _ in range(n+1)]
    is_prime_num[0], is_prime_num[1] = False, False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime_num[i]:
            for j in range(2 * i, n + 1, i):
                is_prime_num[j] = False
    
    return is_prime_num

# def is_prime_num(n):
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True 

import sys 

is_prime_num = get_prime_nums(MAX_NUM)

while True:
    flag = False
    n = int(sys.stdin.readline())
    
    # 마지막 입력
    if n == 0:
        break
    
    # prime_nums, is_prime_num = get_prime_nums(MAX_NUM)
    # print(prime_nums)

    # for num in prime_nums:
    #     print(f'num: {num}')
    #     if is_prime_num[n-num]:
    #         print(f'{n} = {num} + {n-num}')
    #         flag = True
    #         break

    # 두 번째 시도
    for i in range(3, n // 2 + 1, 2):
        if is_prime_num[i] and is_prime_num[n-i]:
            print(f'{n} = {i} + {n-i}')
            flag = True
            break 

    if not flag:
        print("Goldbach's conjecture is wrong.")
    
    