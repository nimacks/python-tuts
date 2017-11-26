
#Exception Handling
"""
Different exceptions are raised for different reasons. 
Common exceptions:
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly; 
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.

"""
num1 =7
num2 = 0
#print(num1/num2)

"""
To handle exceptions, and to call code when an exception occurs, you can use a try/except statement.
The try block contains code that might throw an exception. If that exception occurs, the code in the try block stops being executed, 
and the code in the except block is run. If no error occurs, the code in the except block doesn't run.

"""
try:
   num1 = 7
   num2 = 0
   print (num1 / num2)
   print("Done calculation")
except ZeroDivisionError:
   print("An error occurred")
   print("due to zero division")

   """
A try statement can have multiple different except blocks to handle different exceptions.
Multiple exceptions can also be put into a single except block using parentheses, to have the except block handle all of them.
   """
   try:
       variable =10
       print(variable + "hello")
       print(variable/2)
   except ZeroDivisionError:
       print("Divided by zero")
   except (ValueError,TypeError):
       print("Error Occurred")