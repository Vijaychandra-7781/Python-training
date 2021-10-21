def factorial(num):  # function define
    res=1

    for i in range(2,num+1):
        res=res*i
    print('the factorial of the given number is:',res)

num=int(input('enter yhe number for factorial:'))
factorial(num) # function calling