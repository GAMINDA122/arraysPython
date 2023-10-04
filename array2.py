from array import *

x = array ('i',[2,-3,5,7,9,10])
print("1st array : ",x)
x.append(12)#add only one element after list
print("2nd array : ",x)
x.extend([15,17,19])#add multiple value end of the list
print("3rd array : ",x)
x.insert(1,-5) #enter value from specific space
print("4th array : ",x)#remove last element
x.pop()
print("5th array : ",x)
x.pop(0)#remove specific element
print("6th array : ",x)
x.remove(7)#remove value not use index using value
print("7th array : ",x)
