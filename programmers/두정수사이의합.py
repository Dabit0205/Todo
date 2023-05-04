# 두 정수 a, b가 주어졌을 때 
# a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
# 
# 제한 조건
# a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
# a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
# a와 b의 대소관계는 정해져있지 않습니다.

a1= 3
b1= 5
return1 = 12

a2 = 3 
b2 = 3
return2 = 3

a3= 5
b3= 3
return3 = 12

def solution1(a, b):
    # range(a, b+1) => a부터 b까지의 정수
    answer = sum(range(min(a, b), max(a, b)+1))
    return answer


print(solution1(a1, b1))
print(solution1(a2, b2))
print(solution1(a3, b3))


# 런타임 에러뜨지만 코드를 살펴볼 필요가 있다.
def solution2(a, b):
    result = 0
    if a > b :
        num_list = list(range(b, a+1))
        for i in range(len(num_list)):
            result += num_list[i]
    elif b > a :
        num_list = list(range(a, b+1))
        for i in range(len(num_list)):
            result += num_list[i]
    elif a == b:
        result = a

    # 함수를 완성하세요
    return result

print(solution2(a1, b1))
print(solution2(a2, b2))
print(solution2(a3, b3))