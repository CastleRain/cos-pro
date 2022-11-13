def solution(s):
    answer = ""
    save_text = ""
    for i in s:
        if i == "1":
            if len(save_text) > 0:
                answer += save_text
                save_text = ""
            answer += i
            
        else:
            if len(save_text) == 0:
                save_text += i
    
    if len(save_text) != 0:
        answer += save_text



    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
s = "1011000111001000"
ret = solution(s)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")