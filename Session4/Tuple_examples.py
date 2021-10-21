"""Tuple is a group of value with comma separtaion enclosed with in the paranthesis is called as Tuple.
Tuple is an immutable in nature ,immutable means we can't modify the values.

Tuple is an ordered ,indexed it supports positive indexing and negative indexing also
Examples given below"""
t=(1,2,4,5,6)
print(type(t))#type is used to check the what data type

print('the length of the tuple is:',len(t))#len function used to find the length


# firts we take two tuples
t1=1,2,3,4
t2=(10,20,30,40,1)
print(t1+t2) #tuple allows duplicate value also


#create the empty tuple
t3=()
print(type(t3))

#we can check the values how many times is repeated using count method

t5=(10,20,30,10,330,30,10,23,48)

a=t5.count(10)# 10 how many times repeated
print(a)

#we can check the index position also using the index method

t6=(10,20,30,40,50,30,60)

print(t6.index(30))# 30 which index position

print(t6.index(30,3)) # after 3rd position where will be occured 30

s=set()
d={}
print(type(d))