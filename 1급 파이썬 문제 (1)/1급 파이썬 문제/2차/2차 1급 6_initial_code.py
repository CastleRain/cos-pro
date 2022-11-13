#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(commands):
    # 여기에 코드를 작성해주세요.
    

    move = ["L", "R", "U", "D"]
    dx = [-1, 1, 0, 0]
    dy = [0,0, 1, -1]
    x, y = 0, 0
    for i in commands:
        idx = 0
        for m in move:
            idx += 1
            if m == i:
                x += dx[idx-1]
                y += dy[idx-1]
                break
    answer = [x, y]



    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
commands = "URDDLLL"
ret = solution(commands)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")