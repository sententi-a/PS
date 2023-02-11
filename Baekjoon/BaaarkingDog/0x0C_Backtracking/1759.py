# 암호 만들기 https://acmicpc.net/problem/1759

"""
암호는 서로 다른 L개의 알파벳 소문자들로 구성
최소 한 개의 모음 (a, e, i, o, u)과 최소 두 개의 자음으로 구성
암호를 이루는 알파벳은 오름차순으로 정렬되어 있음
- 즉, abc는 가능성 있지만, bac는 그렇지 않음
암호로 사용했을 법한 문자의 종류는 C가지
가능성 있는 암호들을 모두 구하기
"""

import sys

pw_length, char_count = map(int, sys.stdin.readline().split())
chars = list(map(str, sys.stdin.readline().split()))

chars.sort()

# 중복 없는 선택을 위한 선택 체크용 리스트 
used = [False for _ in range(char_count)]
answer = ['a' for _ in range(pw_length+1)]


def condition_check(arr):
    vowel_cnt = 0

    for char in arr:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowel_cnt += 1
    
    # 최소 한 개 이상의 모음, 두 개 이상의 자음
    if vowel_cnt >= 1 and len(arr) - vowel_cnt >= 2:
        return True
    return False


def sol(cur):
    global pw_length, char_count

    if cur == pw_length:
        if condition_check(answer[:pw_length]):
            print(*answer[:pw_length], sep="")
        return

    for i in range(char_count):
        answer[cur] = chars[i]
            
        if not used[i] and answer[cur] >= answer[cur-1]:
            used[i] = True
            sol(cur+1)
            used[i] = False

sol(0)