# 01타일 https://www.acmicpc.net/problem/1904
import sys
n = int(sys.stdin.readline()) # 크기가 n인 2진 수열

# 테이블 정의 : D[i] = 크기가 i인 2진 수열을 만드는 모든 경우의 수 

# 점화식 : D[k] = D[k-2] + D[k-1]

# D[1] = 1 (1)
# D[2] = 2 (00, 11)
# D[3] = 3 (001, 100, 111)
# D[4] = 5 (0000, 0011, 1100, 1001, 1111)
# D[5] = 8 (00100, 00001, 00111, 10011, 11001, 10000, 11111, 11100) 
"""
문제의 상황에서 맨 앞에 올 수 있는 타일은 2가지 뿐입니다.

00 타일과 1 타일.

00 타일이 올 경우 00..으로 시작하고
1 타일이 올 경우 1...로 시작하겠지요.

이때 '길이가 N인 이진 수열의 개수'를 f(N)이라고 정의합시다.
그러면 경우 (1)의 가짓수는 f(N-2)가 되고 경우 (2)의 가짓수는 f(N-1)이 될 것입니다.
따라서 전체 경우의 수 f(N) 은 경우 (1) 과 (2)의 가짓수의 합인
f(N) = f(N-1) + f(N-2)가 됩니다.

또한 f(0) = f(1) = 1임을 확인할 수 있습니다.
"""

"""tabulation_memory"""
# table = [0 for i in range(n+1)]

# table[1] = 1
# table[2] = 2

# for i in range(3, n+1):
#     table[i] = table[i-2] + table[i-1]

# print(table[n] % 15746)

"""timeout"""
# prev = 1
# current = 2

# for i in range(3, n+1):
#     temp = current
#     current = prev + temp
#     prev = temp

# print(current % 15746)

""""""
table = [0 for i in range(n+1)]
table[1] = 1

if n <= 1:
    print(table[n])
    exit()

table[2] = 2

if n <= 2:
    print(table[n])
    exit()

for i in range(3, n+1):
    table[i] = (table[i-2] + table[i-1]) % 15746 
   
print(table[n])