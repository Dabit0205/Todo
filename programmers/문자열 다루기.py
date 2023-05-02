# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
# 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.


s1 = "a234"
s2 = "1234"
s3 = "a12345"
s4 = "123456"
s5 = "1234567"


def solution(s):
    if len(s) == 4 or len(s) == 6:  # 문자열 길이가 4 혹은 6인지 확인
        if s.isdigit():  # 숫자로만 구성되있는지 확인
            return True
    return False


print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
print(solution(s5))


def solution(s):
    if len(s) != 4 and len(s) != 6: # 문자열 길이가 4 혹은 6인지 확인
        return False
    for i in s:
        if i < '0' or i > '9': # 1~8로 구성되있는지 확인
            return False
    return True


print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
print(solution(s5))
