""" 
문제 설명
문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요

제한사항
1 ≤ my_string의 길이 ≤ 1,00

입출력 예
my_string	return
"jaron"	    "noraj"
"bread"	    "daerb"
"""

def solution(my_string):
    answer = my_string[::-1]
    return answer

print(solution("jaron"))