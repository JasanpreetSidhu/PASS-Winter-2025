# using loop
def sumNumsUpto10():
    #result = 0 + 1 + 2 + 3 + .. + 10
    # 1st result = 0 + 0
    # result = 0 + 1
    # result = result + 2
    # result = result + 3
    result = 0
    for i in range(0,11):
        result = result + i
    return result

print(sumNumsUpto10())
        
