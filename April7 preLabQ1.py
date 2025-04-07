def is_triple(num1, num2, num3):
    # sq(num1) + sq(num2) = sq(num3)
    if (num1*num1 + num2*num2 == num3*num3):
        result = True
    elif (num2*num2 + num3*num3 == num1*num1):
        result = True
    elif (num1*num1 + num3*num3 == num2*num2):
        result = True
    else:
        result = False
    return result

numbers = [3,4,5,1,7,9,6,8,69]

for index in range(0,len(numbers),3):
    # call function for triplets in list
    result = is_triple(numbers[index], numbers[index+1], numbers[index+2])
    if(result == True):
        print("pythogoreas theorem is satisfied")
    else:
        print("not satisfied")
