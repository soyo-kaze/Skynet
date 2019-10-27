# importing libraries
import time
import math


# decorator to calculate duration
# taken by any function.
def sam(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*hah):
        # storing time before function execution
        begin = time.time()

        func(*hah)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end, " ", begin)

    return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@sam
def fact(num,name):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    print("hello \n")
    print(math.factorial(num))


@sam
def yo():
    print("heyo, look into ma eyes!! boo, tsukuyomi!! :V")


yo()
print()
# calling the function.
fact(10,"sameer")
