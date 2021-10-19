l1=[10,4,90,37,80]

print('the minimum value is:',min(l1))#with using method min

print('the maximum value is:',max(l1))# with using method max

#or
def minimum(list):
  min = list[0]  # Start you can assume oth index value is mininimum
  for num in list:       #  in the Loop check each number in the list
    if num < min:
      min = num  # assign to a new min
  return min

print ('the minimum element is',minimum([1,2,3,-1]) ) # -1
