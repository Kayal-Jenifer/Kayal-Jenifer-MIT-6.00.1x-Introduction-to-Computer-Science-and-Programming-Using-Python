# Exercise: while exercise 1

# In this problem you'll be given a chance to practice writing some while loops.

# 1. Convert the following into code that uses a while loop.

# print 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!

# YOUR CODE HERE...

i=2
while(i<=10):
    print(i)
    i+=2
print("Goodbye!")


# Exercise: while exercise 2

# 2. Convert the following into code that uses a while loop.

# prints Hello!
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2

# YOUR CODE HERE...

print("Hello!")
i=10
while(i>=2):
    print(i)
    i-=2



# Exercise: while exercise 3

# 3. Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you.
# So, for example, if we define end to be 6, your code should print out the result: 21
# which is 1 + 2 + 3 + 4 + 5 + 6.

# For problems such as these, do not include input statements or define variables we will provide for you.
# Our automating testing will provide values so write your code in the following box assuming these variables are already defined.

# YOUR CODE HERE...

total = 0
i = 0
while i <= end:
    total += i
    i += 1
print(total)