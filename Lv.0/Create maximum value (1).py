""" 
문제 설명
정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

제한사항
0 ≤ numbers의 원소 ≤ 10,000
2 ≤ numbers의 길이 ≤ 100

입출력 예
numbers	                 result
[1, 2, 3, 4, 5]	        20
[0, 31, 24, 10, 1, 9]	744
"""

def solution(numbers):
    answer = 0
    number_list = []
    
    for a in range(2):
        number_max = max(numbers)
        number_list += [number_max]
        numbers.remove(number_max)
        
    x, y = number_list
    return x*y

a = solution([1, 2, 3, 4, 5])
print(a)