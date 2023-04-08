# 비밀번호 발음하기 https://www.acmicpc.net/problem/4659

"""
1, 모음(a, e, i, o, u) 중 하나를 반드시 포함
2. 모음이 3개 / 자음이 3개 연속으로 오면 안 됨
3. 같은 글자가 연속적으로 2번 오면 안 됨 
    - 단, ee와 oo는 허용
패스워드는 대문자를 포함하지 않음
"""

vowels = set(['a', 'e', 'i', 'o', 'u'])
redundance_ok = set(['e', 'o'])

def check_availability(password: str):
    # First rule #
    password_set = set(password)
    intersect = password_set.intersection(vowels)
    
    if not len(intersect):
        return False

    # Second rule #
    vowel_cnt = 0
    consonant_cnt = 0

    for i in range(len(password)):
        # 현재 보고 있는 알파벳이 모음일 때 
        if password[i] in vowels:
            vowel_cnt += 1

            if i != 0 and password[i-1] not in vowels:
                consonant_cnt = 0

        # 현재 보고 있는 알파벳이 자음일 때 
        else:
            consonant_cnt += 1
            if i!= 0 and password[i-1] in vowels:
                vowel_cnt = 0

        if vowel_cnt == 3 or consonant_cnt == 3:
            return False 
        
       
        # Third rule #
        if i > 0:
            if password[i] not in redundance_ok:
                if password[i-1] == password[i]:
                    return False
    
    return True


import sys

while True:
    password = sys.stdin.readline().rstrip()

    # End of Input
    if password == 'end':
        break
    
    is_available = check_availability(password)

    if is_available:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
