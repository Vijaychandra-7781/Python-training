
"""Frozenset is the freeze the iterable type and make it unchangable means immutable """

# Exmaple list
l1=[10,20,30,40]
print(l1)
l1[1]=25
print(l1)
a=frozenset(l1)
print(a)
print(type(a))

print("*"*100)

#Example set
s1={1,2,3,4,5,6}
print(type(s1))
b=frozenset(s1)
print(type(b))
print(b)
#a[1]=100 after converting frozenset doesn't add  any value it show error

print("*"*100)

#Example dictionary

d1={1:'vijay',2:'chandra',3:'Amal',4:'Faizan'}
print(type(d1))
c=frozenset(d1)# converting to frozenset
print(type(c))
