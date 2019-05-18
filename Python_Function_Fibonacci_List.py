# Python Defining Functions 
# We can create a function that writes the Fibonacci series 
# to an arbitrary boundary:
# The keyword 'def' introduces a function definition.
# In this simple example, the function that returns a list of the numbers 
# of the Fibonacci series, instead of printing it:
# The function makes use of another Python function 'append'
# Note the presence of the 'return' statement which returns 
# with a value from the function.

def fib2(n):      # return Fibonacci series up to n
      """Return a list containing the Fibonacci series up to n."""
       result = []
       a, b = 0, 1
       while a < n:
           result.append(a)    # see below
            a, b = b, a+b
       return result

f100 = fib2(100)    # call it
f100                # write the result
