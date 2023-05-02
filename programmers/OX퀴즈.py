# 덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다.
# 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.

quiz1 = ["3 - 4 = -3", "5 + 6 = 11"]
result1 = ["X", "O"]

quiz2 = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]
result2 = ["O", "O", "X", "O"]


def solution1(quiz):
    answer = []
    for equation in quiz:
        x, operator, y, _, z = equation.split()  # 문자열을 공백으로 나눠서 각각의 값을 변수에 할당
        if operator == "+":
            if int(x) + int(y) == int(z):
                answer.append("O")
            else:
                answer.append("X")
        else:                                   # operator == "-"
            if int(x) - int(y) == int(z):
                answer.append("O")
            else:
                answer.append("X")
    return answer


print(solution1(quiz1))
print(solution1(quiz2))


def solution3(quiz):
    answer = []
    bool_to_OX = {False: 'X', True: 'O'}
    for equation in quiz:
        a, operator, b, equal_sign, c = equation.split()           # 수식 분리
        a, b, c = int(a), int(b), int(c)
        if operator == "+":
            answer.append(bool_to_OX[a+b == c])
        else:                                               # operator == "-"
            answer.append(bool_to_OX[a-b == c])
    return answer


print(solution3(quiz1))
print(solution3(quiz2))
