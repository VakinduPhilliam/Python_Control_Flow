# Python Defining Functions (Default Argument Values)
# It is also possible to define functions with a variable number of arguments.
# This creates a function that can be called with fewer arguments than
# it is defined to allow.

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
      ok = input(prompt)
      if ok in ('y', 'ye', 'yes'):
       return True
       if ok in ('n', 'no', 'nop', 'nope'):
         return False
         retries = retries - 1
        if retries < 0:
         raise ValueError('invalid user response')
     print(reminder)
