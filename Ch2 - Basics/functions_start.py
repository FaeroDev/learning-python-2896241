#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def func1():
    print("I am a function")


func1()
print(func1())
print(func1)

# TODO: function that takes arguments


def func2(arg1, arg2):
    print(arg1, " ", arg2)


func2("hello", "there")

# TODO: function that returns a value


def cube(x):
    return x * x * x


print(cube(2))

cubeRes = cube(5)
print(cubeRes)

# TODO: function with default value for an argument


def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


print(power(2))
print(power(2, 5))

print(power(x=3, num=2))
# TODO: function with variable number of arguments


def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


print(multi_add(4, 5, 10, 200))
