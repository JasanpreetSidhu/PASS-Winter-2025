def calculation(a, b=5):
    add = a + b
    subtraction = a - b
    return add, subtraction

# saving returns values into individual variables
res1, res2 = calculation(40,10)
print(res1, res2)

print(calculation(40,10))

# calculation function returns tuple format
res = calculation(40,10)
# displaying single value
for i in res:
    print(i)

res3, res4 = calculation(10)
print(res3,res4)
    
