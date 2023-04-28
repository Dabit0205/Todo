# 영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다.
# 문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔
# return 하도록 solution 함수를 완성해 주세요.

# 메서드를 사용하여 푸는 방식으로
# replace 함수
# 문자열.replace(바꿀 문자열, 새로운 문자열, [바꿀 횟수])

# 딕셔너리를 만들고, for 루프를 사용하여 딕셔너리의 키와 값을 사용하여
# 문자열에서 영어 숫자를 찾아 해당하는 정수 값으로 대체합니다.
# 마지막으로, 문자열을 정수로 변환하여 반환합니다

numbers1 = "onetwothreefourfivesixseveneightnine"
numbers2 = "onefourzerosixseven"


def solution(numbers):
    # 영어 숫자와 해당하는 정수 값을 딕셔너리에 저장합니다.
    num_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    # 문자열 numbers에서 영어 숫자를 해당하는 정수 값으로 바꿉니다.
    for word, num in num_dict.items():
        numbers = numbers.replace(word, str(num))
    # 바꾼 문자열을 정수로 변환하여 반환합니다.
    return int(numbers)


print(solution(numbers1))
print(solution(numbers2))


def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)


print(solution(numbers1))
print(solution(numbers2))
