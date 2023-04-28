# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을
# return하도록 solution 함수를 완성해주세요

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [0, 31, 24, 10, 1, 9]


def solution(numbers):
    # 리스트 정렬
    numbers.sort()
    return numbers[-1]*numbers[-2]


print(solution(numbers1))
print(solution(numbers2))
