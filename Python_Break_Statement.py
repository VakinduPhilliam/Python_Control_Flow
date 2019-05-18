# Python 'break' statement
# The break statement, like in C, breaks out of the innermost 
# enclosing for or while loop.
# Yes, this is the correct code. 
# Look closely: the else clause belongs to the for loop, not the if statement
# Python Loop statements may have an 'else' clause; it is executed when the loop terminates 
# through exhaustion of the list (with for) or when the condition becomes false 
# (with while), but not when the loop is terminated by a break statement. 

for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
      else:
          # loop fell through without finding a factor
          print(n, 'is a prime number')

