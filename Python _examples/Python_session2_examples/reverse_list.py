l1=[10,20,30,40,50]
l2=[]# empty list
for i in range(len(l1)-1,-1,-1):# this is one way of reverse list
    l2.append(l1[i])
print(l2)
# Anotheer way using slicing is used to get the partial data
#or slicing also used for the reverse list
print(l1[::-1])