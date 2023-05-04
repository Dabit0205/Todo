# 문자열 my_string이 매개변수로 주어질 때, 
# 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 
# solution 함수를 완성해주세요.

	
my_string1 = "cccCCC"	
result1 = "CCCccc"

my_string2 = "abCdEfghIJ"	
result2 = "ABcDeFGHij"

def solution1(my_string):
    answer = ''
    for i in my_string:
        # i가 전부소문자인지 체크, 소문자면 upper 후 answer에 추가
        if i.islower():
            answer += i.upper()
        # 대문자면 lower 후 answer에 추가
        else:
            answer += i.lower()
    return answer

def solution2(my_string):
    answer = ''
    return answer.join([x.lower() if x.isupper() else x.upper() for x in my_string])


def solution3(my_string):
    answer = ""
    return answer.join(map(lambda s: s.upper() if s.islower() else s.lower(), my_string))

def solution4(my_string):
    # swapcase() 문자열에서 대문자를 소문자로, 소문자를 대문자로 바꿔주는 메서드입니다.
    answer = my_string.swapcase()
    return answer


print(solution1(my_string1))
print(solution1(my_string2))

print(solution2(my_string1))
print(solution2(my_string2))

print(solution3(my_string1))
print(solution3(my_string2))

print(solution4(my_string1))
print(solution4(my_string2))