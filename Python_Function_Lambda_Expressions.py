# Python Function Lambda Expressions
# Small anonymous functions can be created with the lambda keyword. 
# This function returns the sum of its two arguments: lambda a, b: a+b. 
# Lambda functions can be used wherever function objects are required.

def make_incrementor(n):
       return lambda x: x + n

 f = make_incrementor(42)
 f(0)
 f(1)
