# simple_function.py[l]
# Simple function test for Pyylisp.

# All this does is define and run a simple function, something
# essential to any programming language. Note that the Pyylisp
# function skips the parentheses of the Python function, and also
# lacks the return keyword.

def square(number)
	return number ** 2

# Note that parentheses are required for the inner function call,
# since otherwise print would print the function and 3 instead of the
# result of calling the function with 3.

print(square 3)
