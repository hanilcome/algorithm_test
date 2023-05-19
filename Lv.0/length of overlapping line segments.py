""" 
문제 설명
선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

lines가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.

제한사항
lines의 길이 = 3
lines의 원소의 길이 = 2
모든 선분은 길이가 1 이상입니다.
lines의 원소는 [a, b] 형태이며, a, b는 각각 선분의 양 끝점 입니다.
-100 ≤ a < b ≤ 100

입출력 예
lines	                    result
[[0, 1], [2, 5], [3, 9]]	2
[[-1, 1], [1, 3], [3, 9]]	0
[[0, 5], [3, 9], [1, 10]]	8
"""
# 첫번째 시도 코드
# def solution(lines):
#         answer = 0
#         x, y, z = lines
#         arr = []
#         arr1 = []
#         arr2 = []
#         arr3 = []

        
#         for a in range(x[0], x[1]+1):
#                 arr += [a]
#         for a in range(y[0], y[1]+1):
#                 arr += [a]
#         for a in range(z[0], z[1]+1):
#                 arr += [a]
        

#         print(arr)
#         for a in arr:
#                 if a not in arr1:
#                         arr1 += [a]
#                 else:
#                         arr2 += [a]
#                         answer += 1
#         for a in arr2:
#                 if a not in arr3:
#                         arr3 += [a]
#                 else:
#                         answer -= 1
        
#         if x[1] == y[0]:
#                 answer -= 1
#         if y[1] == z[0]:
#                 answer -= 1
#         if answer > 1:
#                 answer -= 1
#         print(arr1)
#         print(arr2)
#         return answer

# 정답코드(14점)
def solution(lines):
        answer = 0
        arr = []
        x, y, z = lines

        
        for a in lines:
                arr += a
        nmax = max(arr)
        nmin = min(arr)
        print(x, y, z, nmin, nmax)
        print(arr)

        for i in range(nmin, nmax+1):
                count = 0

                if x[0] <= i < x[1]:
                        count += 1
                if y[0] <= i < y[1]:
                        count += 1
                if z[0] <= i < z[1]:
                        count += 1

                if count >= 2:
                        answer += 1

        return answer

a = solution([[0, 5], [3, 9], [1, 10]])
print(a)

