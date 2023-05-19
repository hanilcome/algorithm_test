""" 
문제 설명
가위는 2 바위는 0 보는 5로 표현합니다. 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.

제한사항
0 < rsp의 길이 ≤ 100
rsp와 길이가 같은 문자열을 return 합니다.
rsp는 숫자 0, 2, 5로 이루어져 있습니다.

입출력 예
rsp	    result
"2"	    0"
"205"	"052"
"""

def solution(rsp):
    answer = rsp
    win = ''
    for a in rsp:
        if a == "2":
            win += "0"
        elif a == "0":
            win += "5"
        elif a == "5":
            win += "2"
    return win
    

a = solution("205")
print(a)