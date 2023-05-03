# 문자열 my_string이 매개변수로 주어집니다.
# my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을
# return하도록 solution 함수를 완성해주세요.

my_string1 = "people"
my_string2 = "We are the world"


def solution(my_string):
    answer = ''.join(list(dict.fromkeys(my_string)))  # dict으로 중복을 제거한 리스트
    return answer


print(solution(my_string1))
print(solution(my_string2))


def solution2(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer


print(solution2(my_string1))
print(solution2(my_string2))


def solution3(my_string):
    answer = ''.join([i for n, i in enumerate(
        my_string) if i not in my_string[:n]])
    return answer


print(solution3(my_string1))
print(solution3(my_string2))
