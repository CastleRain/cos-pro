#You may use import as below.
#import math

def solution(num):
    # Write code here.
    answer = ""
    num += 1

    for i in str(num):
        if i == "0":
            answer += "1"
        else:
            answer += i

    answer = int(answer)



    return answer


#The following is code to output testcase.
num = 9949989;
ret = solution(num)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")