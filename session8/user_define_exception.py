"""Programmers may name their own exceptions by creating a new exception class. Exceptions need to be derived

 from the Exception class, either directly or indirectly. Although not mandatory, most of the exceptions

 are named as names that end in “Error” similar to the naming of the standard exceptions in python.


  If we want to throw an  user define class object the class must have exception properties  otherwise
  python throws an syntax error """


# This is the Example for how to create your own exception

class InvalidNumberError(ZeroDivisionError): # you can give exception or base exception

    def __init__(self,message):
        self.message=message

        print('running init method')

num1=10
num2=0
res=0
try:
    if num2==0:
        raise InvalidNumberError('denominantor cannot be zero')

    else:
        res=num1/num2

        print('result is:',res)

except InvalidNumberError as ine:
    print(ine)



#Another example

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()


print("Congratulations! You guessed it correctly.")