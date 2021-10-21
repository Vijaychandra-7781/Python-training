"""write a program to sort the dictionary"""


def sort_dict(dict):# functiond definition

    p=sorted(dict.values())# sorted method is used for sort the dictionary
    print('the sorted dictionary is:',p)

sort_dict(dict={1:'vijay',3:'amal',4:'abbas',2:'faizan',5:'mukund'}) # function calling