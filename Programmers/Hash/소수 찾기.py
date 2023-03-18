from math import sqrt
from itertools import permutations

def check_prime_num(num):
    result = [True for _ in range(num+1)]
    # 1은 소수가 아니므로
    result[0], result[1] = False, False
    
    for i in range(2, int(sqrt(num+1))):
        if result[i]:
            for j in range(2*i, num+1, i):
                result[j] = False

    return result

def solution(numbers):
    numbers = list(numbers)
    nums_length = len(numbers)
    
    new_list = sorted(numbers, reverse=True)
    max_num = int(''.join(new_list))
    
    is_prime_num = check_prime_num(max_num)
    
    answer = []
    
    for i in range(1, nums_length + 1):
        for case in permutations(numbers, i):
            number = ''.join(case).lstrip('0')
            
            if number == '':
                continue
            
            number = int(number)
            
            if is_prime_num[number] and number not in answer:
                answer.append(number) 
    return len(answer)