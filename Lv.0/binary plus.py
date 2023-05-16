"""
--다시 풀기--

문제 설명
이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

제한사항
return 값은 이진수를 의미하는 문자열입니다.
1 ≤ bin1, bin2의 길이 ≤ 10
bin1과 bin2는 0과 1로만 이루어져 있습니다.
bin1과 bin2는 "0"을 제외하고 0으로 시작하지 않습니다.

입출력 예
bin1	bin2	result
"10"	"11"	"101"
"1001"	"1111"	"11000"
"""
def solution(bin1, bin2):
    answer = ''
    sum = 0
    n = 1
    share = 0
    
    if bin1 != '0' and bin2 != '0':
        for s in range(len(bin1)-1, -1,-1):
            sum = sum + int(bin1[s])*n
            n = n*2

        n = 1   
        for s in range(len(bin2)-1, -1,-1):
            sum = sum + int(bin2[s])*n
            n = n*2
            
            
        while(share != 1):
            share = sum // 2
            rest = sum % 2
            sum = share
            answer += str(rest)
            
        answer += str(share)
    
    return answer[::-1]