# write program that asks user for two numbers
# and adds them and displays the result

input1 = input("Enter number 1: ")
num1 = int(input1)
num2 = int(input("Enter number 2: "))
total = num1 + num2
print(total)


# converting above program to function that
# returns the result and then call that function

def addTwoNumbers(num1, num2):
    result = num1 + num2
    return result

output = addTwoNumbers(num1, num2)
print(output)
print("Call function directly: ", addTwoNumbers(3,4))

    
    

