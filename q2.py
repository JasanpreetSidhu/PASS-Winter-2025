# args = ["value1", "value2"]
def displayValue(*args):
    for i in args:
        print(i)
    print(args)

displayValue("HTML", "Python")
displayValue("a", "b", "c")
