"""First will go to Types of termination
1.Normal termination : Executing all the line after the termination occur this is called as norml termination
Example

l=[1,2,3,4,56,7,8,9,10]
for i in l:
if l[i]%2==0:
print('even')
else:
print('odd')


2.Force termination: In this termination if condition is satisfy terminate the code suddenly
is called as force termination   with using the exit() keyword is used to force termination

Example
l=[1,2,3,4,5,2,5,6]
for i in l:
if l[i]==2:
exit()


3.Abrupt termination: Due to disturbance python will terminate the execution is called as abrupt termination




what is an exception

exception is an event which disturbs the flow of program execution the program get terminate abruptly
is called as  exception.

Due to this abrupt termination the data and objects stored in the memory will be lost

"Exception handling is the proces of handling the error when the exception event occured in the execution
is called is exception handling"

The handler will handle the error in such a way that the program continue the execution and terminate
normally even after error is occured.


All exception types inherits from  super class by name  base exception.

Baase exception class defines the properties of any exception types


why is important
Because, Exception handling allows you to separate error-handling code from normal code.

An exception is a Python object which represents an error.

An exception is a convenient method for handling error messages.

 As with code comments, exceptions helps you to remind yourself of what the program expects.

"""

# How to handle the error


num1=int(input('enter the numer:'))
num2=int(input('enter the number:'))
res=0
res=num1/num2
print('the result is:',res)

print('*'*100)

# Example

num1=10
num2=2# in num2 we give value greater than zero is not getting any error it directly goes print the result
res=0
try:
    res=num1/num2  # in this statement will getting the error
except ZeroDivisionError:
    print("can't divided by zero denominator should be non zero number" )
print('the result is:',res)

print('*'*100)
# Handle in the function body

def div(numerator,denominator):
    res=None
    try:   #if try block success else condition will be executed otherwise its not executed
        res=numerator/denominator

    except:
        print("denominator can't be zero")
        # res=numerator/1

n1=int(input('enter the number:'))
n2=int(input('enter the number:'))
div(n1,n2)
print('the result is',res)

print('*'*100)


# Another example using else

try:
    #this will throw an exception if the file doesn't exist.
    filename = open("file.txt","r")

except IOError:
    print("File not found")

else:
    print("The file opened successfully")
    filename.close()

print('*'*100)
#Error occur in the function body but handling in main function


def div(numerator,denominator):

    res=None
    res=numerator/denominator
    print('result is:',res)

num1=int(input('entr the number:'))
num2=int(input('enter the number:'))

try:
    div(num1,num2)

except ZeroDivisionError:
    print('error in division denominator to give non zero')
    num2=int(input('enter the number'))
    div(num1,num2)

finally:   #If try and except block surrounded by finally block the python guarantee
    #that statement of finally block would be executed in all the scenario
    print('it is always running')

print('*'*100)




# try and except nested also running


try:
    num1=int(input('enter the number:'))
    num2=int(input('enter the numer:'))

    div(num1,num2)
except ZeroDivisionError:

    print('error in division please give non zero number')

    num2=int(input('enter the number:'))
    div(num1,num2)

except ValueError:

    print('doesnot accept the string')
    num2=(input('enter the number:'))
    div(num1,num2)

    try:

        div(num1,num2)

    except ZeroDivisionError:
        print('error in division')
        num2=int(input('enter non zero number'))

        div(num1,num2)
finally:

    print('it is always run')
print('*'*100)

# another example using else statement




num1=10
num2=1

res=0
try:

    print('enter the try block')
    res=num1/num2
    print('exit try block')

except ZeroDivisionError:

    print('denominator should be non zero')

else:
    print('any operation is permitted')
#The finally block is everytime is running but else block when try block success on that time only
#execute otherwise doesnot execue


finally:
    print('everytime is running')
print('*'*100)

"""Note:In except block doesnot give any error name it is capable to find all the errors.

except(Attribute error ,key error) in this one give only access this type of error  any other error occur
it doesnot access because mention these errors only"""






"""what is Raise
The raise keyword is used to raise an exception.

You can define what kind of error to raise, and the text to print to the user.

syntax:  raise error/exception object

raise is also used  out of try and except block"""

# example

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

print('*'*100)



#another example


x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")


print('*'*100)


# another example

num1=10
num2=0
res=0

try:

    if num2==0:
        raise ZeroDivisionError('denominator cannot be zero')
    else:
        res=num1/num2
        print('resrult is:',res)
except ZeroDivisionError as zde :
    print(zde)