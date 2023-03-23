"""
1st try - permutations : fail
2nd try - 모두 동일한 자릿수에 맞춰 숫자를 만들고, 그 숫자를 내림차순으로 정렬
3rd try - 모두 동일한 자릿수에 맞춰 숫자를 만들되, 자릿수에 따라 뒤에 덧붙이는 숫자를 달리함
 자릿수가 0일 때 - int(str(해당 수 * 4))
 자릿수가 1일 때 - int(str(해당 수 * 2))
 자릿수가 2일 때 - int(str(해당 수) + str(해당 수[0]))
"""
# from itertools import permutations

# def solution(numbers):
#     max_num = 0
#     numbers = list(map(str, numbers))
    
#     for case in permutations(numbers, len(numbers)-1):
#         number = "".join(list(map(str, case)))
        
#         max_num = max(max_num, int(number))
#         # print(max_num)
       
#     return str(max_num)

from math import log10

def solution(numbers):
    answer = ''

    if len(numbers) == 1:
        return numbers[0]

    if sum(numbers) == 0:
        return '0'
     
    new_numbers = []

    for number in numbers:
        # log10_0은 성립하지 않음
        if number == 0:
            new_numbers.append((0, '0'))
            continue

        digit = int(log10(number))
        if digit < 3:
            if digit == 0:
                temp_num = int(str(number) * 4)
            elif digit == 1: 
                temp_num = int(str(number) * 2)
            elif digit == 2:
                temp_num = int(str(number) + str(number)[0])
        else:
            temp_num = number

        print(temp_num)
        new_numbers.append((temp_num, str(number)))
         
    new_numbers.sort(key = lambda x : -x[0])
        
    for number in new_numbers:
        answer += number[1]
    
    return answer


# print(solution([100, 101, 1000]))
# print(solution([1, 10, 100, 1000, 818, 81, 898, 89, 0, 0]))
print(solution([0, 0, 0, 0]))
# 8989881881110100100000
# 89 898 818 81 1 10 100 100000 0 0 

# 현재 답 : 8988981881110100100000

# 3 38 383 
# 7 72 727 724
# 72 727
# 727 72 -> 7277, 7272 비교하므로 

# 5(555) 57(57) 500(5) 