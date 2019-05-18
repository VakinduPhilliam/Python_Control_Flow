# Python Functions Unpacking Argument Lists
# The reverse situation occurs when the arguments are already in a list 
# or tuple but need to be unpacked for a function call requiring separate positional arguments.

list(range(3, 6))  # normal call with separate arguments
    args = [3, 6]
    list(range(*args)) # call with arguments unpacked from a list




