#You may use import as below.
#import math

def solution(pos):
    # Write code here.
    answer = 0
    m = int(pos[1]) - 1
    n = int(ord(pos[0])) - int(ord("A"))

    moves = [(1, 2), (1,-2), (-1, 2), (-1,-2), (2,1) ,(2,-1), (-2,1), (-2,-1)]

    for move in moves:
        if 0 <= m-move[0] <= 7 and 0 <= n-move[1] <= 7:
            answer +=1

    
    return answer

#The following is code to output testcase.
pos = "A1"
ret = solution(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")