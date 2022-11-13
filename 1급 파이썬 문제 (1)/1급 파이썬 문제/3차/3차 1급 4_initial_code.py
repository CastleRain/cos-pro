# 다음과 같이 import를 사용할 수 있습니다.
# import math

def sol4(s1, s2):
    cnt = 0
    while True:
        if s1[len(s1)-cnt:] == s2[:cnt]:
            cnt += 1
        else:
            return cnt

def solution(s1, s2):
    # 여기에 코드를 작성해주세요.
    answer = max(sol4(s1, s2), sol4(s2, s1))

        
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")