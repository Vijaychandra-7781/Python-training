"""Entity containing another entity is called as Has a relationship

Two types
1.composition : Full dependency

example:we can take smart phone,smart phone full dependent on battery and internal ram

2.Aggregation:Not dependent

Example:We can take again smart phone Its not dependent with camera, sim


Example of Has a relation

Ball pen has a refill  in this statement ball pen and refill both are the object.

Car has a engine

library has a book"""

# Example of the has a relation

class address:

    def __init__(self,houseno,streetname,areaname,pincode):
        self.houseno=houseno
        self.streetname=streetname
        self.areaname=areaname
        self.pincode=pincode

class customer:
    def __init__(self,name,phoneno,email,houseno,streetname,areaname,pincode):
        self.name=name
        self.phoneno=phoneno
        self.email=email
        self.addr=address(houseno=houseno,streetname=streetname,areaname=areaname,pincode=pincode)

    def details(self):
        print('customer name:',self.name)
        print('customer phoneno:',self.phoneno)
        print('customer email:',self.email)
        print('customer houseno:',self.addr.houseno)
        print('customer streetname:',self.addr.streetname)
        print('customer areaname:',self.addr.areaname)
        print('customer pincode:',self.addr.pincode)

name=input('enter the name:')
phoneno=int(input('enter the phoneno:'))
email=input('enter email:')
houseno=int(input('enter the houseno:'))
streetname=input('enter the streetname:')
areaname=input('enter the areaname:')
pincode=input('enter the pincode:')

c1=customer(name,phoneno,email,houseno,streetname,areaname,pincode)

c1.details()

print('*'*100)


# Another example of Has a realtionship

class employee:

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

class employeedb: # employee db has all the details about employees

    def __init__(self,name,age,gender,empid,email,salary):

        self.empid=empid
        self.email=email
        self.salary=salary
        self.emp=employee(name=name,age=age,gender=gender) # this is another way to create an object inside the class

    def employee_details(self):
        print('employee name:',self.emp.name)
        print('employee age:',self.emp.age)
        print('employee gender:',self.emp.gender)
        print('employee empid:',self.empid)
        print('employee email:',self.email)
        print('employee salary:',self.salary)

name=input('enter the name:')
age=int(input('enter the age:'))
gender=input('enter the gender:')
empid=int(input('enter the empid:'))
email=input('enter the email:')
salary=float(input('enter the salary:'))

e1=employeedb(name,age,gender,empid,email,salary)

e1.employee_details()


