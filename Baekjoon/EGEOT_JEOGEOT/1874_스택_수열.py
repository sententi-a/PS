# 스택 수열 https://www.acmicpc.net/problem/1874

"""
1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써 하나의 수열을 만들 수 있음 (push 순서는 오름차순)
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력
push + pop - 불가능 NO
"""

import sys

# 수열을 담은 배열
nums = []

for _ in range(int(sys.stdin.readline())):
    nums.append(int(sys.stdin.readline()))

prev = 0  # 마지막으로 push한 숫자
stack = []
answers = []

for num in nums:
    if prev < num:
        # 바로 직전 push 했던 마지막 수 + 1부터 해당 num까지 push
        for i in range(prev + 1, num + 1):
            stack.append(i)
            answers.append("+")

        # 한 번 pop으로 빼주기
        stack.pop()
        answers.append("-")
        # 마지막으로 push한 숫자 갱신
        prev = num

    else:
        # pop을 해주되, 그 숫자가 수열에 맞지 않으면 NO 출력
        if stack.pop() != num:
            print("NO")
            exit()

        answers.append("-")

print(*answers, sep="\n")
