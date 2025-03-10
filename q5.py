def doSomething(a, b):
    def doAddition():
        # a, b is defined from outer function
        result = a + b
        return result
    # calling inner function
    res = doAddition()
    return res + 5

print(doSomething(2,3))
