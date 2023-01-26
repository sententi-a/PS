# 재귀함수가 뭔가요? https://acmicpc.net/problem/17478

"""
자동 응답 챗봇의 응답을 출력
출력을 원하는 재귀 횟수 N이 주어지면
출력 예시를 보고 재귀 횟수에 따른 챗봇의 응답 출력
"""

import sys 

count = int(sys.stdin.readline())

def sol(n):
    response1(n-1)
    dashes = '_' * (4 * n)
    print(dashes + '"재귀함수가 뭔가요?"')
    print(dashes + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    response2(n)


def response1(n):

    if n < 0:
        print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
        return
    
    dashes = '_' * (4 * n)
    
    response1(n-1)
    print(dashes+'"재귀함수가 뭔가요?"')
    print(dashes+'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print(dashes+'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print(dashes+'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')

   
def response2(n):
    if n <= 0:
        print('라고 답변하였지.')
        return
    dashes = '_' * (4 * n)
    print(dashes + '라고 답변하였지.')
    response2(n-1)


sol(count)