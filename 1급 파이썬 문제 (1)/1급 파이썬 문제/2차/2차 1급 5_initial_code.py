#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(arr):
    #여기에 코드를 작성해주세요.
    answer = 0

    MIN = -100000009
    min_data = MIN
    save_data = 0
    for i in arr:
        if min_data < i:
            min_data = i
            save_data += 1
        else:
            answer = max(save_data, answer)
            min_data = i
            save_data = 1
        

    answer = max(save_data, answer)

        
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [3, 1, 2, 5, 1, 2, 2, 3,3, 4,5,5,6,7,7,8]
ret = solution(arr)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")