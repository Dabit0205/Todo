rsp1 = "2"
rsp2 = "205"


def solution(rsp):
    answer = ''
    for i in rsp:
        if i == "2":
            answer += '0'
        elif i == "0":
            answer += '5'
        elif i == "5":
            answer += '2'
    return answer


result1 = solution(rsp1)
print(result1)
result2 = solution(rsp2)
print(result2)
