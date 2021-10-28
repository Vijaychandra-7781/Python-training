"""An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the
methods __iter__() and __next__().

Iterator is the proces of traversing a each value  one by one is called as Iterator"""

# Normally we can iterate  the value using the for loop

l1=[1,2,3,44,56,77,88]
print(l1)

for num in l1:  # with using the for loop one by one value iterated
    print(num)

print('*'*100)
"""with using the __iter__ and __next__  and next()  method we have to iterate the value"""

l2=[10,29,30,8,6,57,89,46,90]

print(type(l2))  # normally shows list


i_iter=l2.__iter__()
print(type(i_iter)) # check the type is converting list iterator

print(i_iter.__next__())
print(i_iter.__next__())
print(i_iter.__next__())
print(i_iter.__next__())
print(i_iter.__next__())
print(i_iter.__next__())
print(i_iter.__next__())
print(i_iter.__next__())
print(i_iter.__next__())
# once iterate all the values it shows stop iteration


# Another example

nums=(1,33,44,55,666,77,88)

print(type(nums))

i_nums=nums.__iter__()
print(type(i_nums)) # converting iterator type

print(i_nums) # it shows the address

while True: # all the values iterating after come out of the loop
    try:
        num=next(i_nums)  # this is the another way of iteration using next()
        print(num)
    except StopIteration:
        break

# another example

mystr = "vijay chandra"
myit = iter(mystr) # this is the another way to define iterator method


print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
# print(next(myit))# once you complte iteration it gives any extra next method it shows the error like stop iteration



# Another example

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
