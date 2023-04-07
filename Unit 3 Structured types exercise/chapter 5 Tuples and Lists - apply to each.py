# Exercise: apply to each 1

# Here is the code for a function applyToEach:

# def applyToEach(L, f):
#     for i in range(len(L)):
#         L[i] = f(L[i])

# Assume that
# testList = [1, -4, 8, -9]

# For each of the following questions (which you may assume is evaluated independently of the previous questions, so that testList
# has the value indicated above), provide an expression using applyToEach, so that after evaluation testList has the indicated
# value. You may need to write a simple procedure in each question to help with this process.

# >>> print(testList)
#    [1, 4, 8, 9]

# Your Code Here...

def absolute (a):
    return abs(a)
applyToEach(testList,absolute)


# Exercise: apply to each 2

# >>> print(testList)
#     [2, -3, 9, -8]

# Your Code Here...

def add(a):
    return a+1
applyToEach(testList,add)


# Exercise: apply to each 3

# >>> print testList
#    [1, 16, 64, 81]

# Your Code Here...

def square(a):
    return a**2
applyToEach(testList,square)