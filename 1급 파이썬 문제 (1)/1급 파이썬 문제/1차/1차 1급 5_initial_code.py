"""
#문제5
다음과 같이 n x n 크기의 격자에 1부터 n x n까지의 수가 하나씩 있습니다.
![image](http://res.cloudinary.com/sgc109/image/upload/c_scale,w_300/v1517462270/%EA%B7%B8%EB%A6%BC1_qysbr6.png)
이때 수가 다음과 같은 순서로 배치되어있다면 이것을 n-소용돌이 수라고 부릅니다.
![image](http://res.cloudinary.com/sgc109/image/upload/c_scale,w_300/v1517462270/%EA%B7%B8%EB%A6%BC2_ol8snc.png)
소용돌이 수에서 1행 1열부터 n 행 n 열까지 대각선상에 존재하는 수들의 합을 구해야 합니다.
![image](http://res.cloudinary.com/sgc109/image/upload/c_scale,w_300/v1517462270/%EA%B7%B8%EB%A6%BC3_cbcdg3.png)
위의 예에서 대각선상에 존재하는 수의 합은 15입니다.
격자의 크기 n이 주어질 때 n-소용돌이 수의 대각선상에 존재하는 수들의 합을 return 하도록 solution 함수를 완성해주세요.

---
##### 매개변수 설명
격자의 크기 n이 solution 함수의 매개변수로 주어집니다.

* n은 1 이상 100 이하의 자연수입니다.

---
##### return 값 설명
n-소용돌이 수의 대각선상에 존재하는 수들의 합을 return 해주세요.

---
##### 예시

| n 	| return 	|
|---	|--------	|
| 3 	| 15     	|
| 2 	| 4      	|

##### 예시 설명
예시 #1
문제의 예와 같습니다.

예시 #2
![image](http://res.cloudinary.com/sgc109/image/upload/c_scale,w_300/v1517462270/%EA%B7%B8%EB%A6%BC4_astq7q.png)
1과 3을 더하여 4가 됩니다.

"""


#You may use import as below.
#import math

def solution(n):
    # Write code here.


    board = [[0] * n for _ in range(n)]
    
    cnt = 1
    x, y = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    idx = 0
    
    while True:
        if board[x][y] == 0: # 처음 들어옴
            board[x][y] = cnt
            cnt += 1

            if 0 <= x + dx[idx] < n and 0 <= y + dy[idx] < n:
                x += dx[idx]
                y += dy[idx]
            else:
                idx = (idx + 1) % 4
        else:

        

    

    answer = 0
    return board


#The following is code to output testcase.
n1 = 3
ret1 = solution(n1)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret1, ".")
    
n2 = 2
ret2 = solution(n2)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret2, ".")