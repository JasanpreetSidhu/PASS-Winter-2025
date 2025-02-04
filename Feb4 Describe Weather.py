# ask user to enter temperature
# assume user enters decimal numbers or float numbers
temperature = input("Enter temperature (in celsius): ")
temperature = float(temperature)
# check if temp is less than -15
if temperature < -15:
    print("Extremely cold")
# temp higher than -15 but less than -1
elif temperature < -1:
    print("Freezing cold")
elif temperature < 5:
    print("very cold")
elif temperature < 10:
    print("cold")
elif temperature < 15:
    print("chilly")
elif temperature < 25:
    print("pleasant")
else:
    print("Hot")
    

