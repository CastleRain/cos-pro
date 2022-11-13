#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(bishops):
    #여기에 코드를 작성해주세요.
    answer = 0

    board = [[0] * 8 for _ in range(8)]

    x = 0
    y = 0

    dx = [-1, -1, 1, 1]
    dy = [1, -1, 1, -1]

    for bishop in bishops:
        first_x = int(ord(bishop[0]) - ord("A"))
        first_y = int(bishop[1]) - 1
        board[first_x][first_y] = 1

        for i in range(4):
            x = first_x
            y = first_y
            while True:
                if 0 <= x + dx[i] <= 7 and 0 <= y + dy[i] <= 7:
                    x += dx[i]
                    y += dy[i]

                    board[x][y] = 1
                else:
                    break

    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                answer += 1

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
bishops1 = ["D5"]
ret1 = solution(bishops1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")