# Max of three numbers
num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
num3 = input("Enter num3: ")

num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

if (num1 > num2):
    if (num1 > num3):
        print(num1)
    else:
        print(num3)
elif (num2 > num3):
    print(num2)
else:
    print(num3)
