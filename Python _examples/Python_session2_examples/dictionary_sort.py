dict={"vijay":67, "mukund": 54, "faizan": 87, "amal": 43, "abbas":73}#create dictionary

print('ascending order values')
p=sorted(dict.values())# with  using the sorting function we can sort the values
print(p)
print('ascending order keys')
q=sorted(dict.keys()) # with  using the sorting function we can sort the values
print(q)
print('descending order values')
p1=reversed(sorted(dict.values()))# reversed is used to print the reverse order the values
for i in p1:
    print(i)
print('descending order keys')
q1=reversed(sorted(dict.keys())) # reversed is used to print the reverse order the values
for j in q1:
    print(j)