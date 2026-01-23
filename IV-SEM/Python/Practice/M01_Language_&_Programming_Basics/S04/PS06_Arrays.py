'''#declaring an array
lis = [1,12.5,True,1,"Python",2+5j]
print(lis,type(lis))
count = 0

#for loop for counter
for _ in lis:
    count+=1
print(count)

#length count for counter 
print(len(lis))

#updating
lis[2] = False
print(lis)

#Adding element - using append element
lis.append(2)
print(lis)

#Inserting element in the list 

lis.insert(3,"RohanJ")
print(lis)

#adding list element at the index not present 
#so it will apend at last
lis.insert(20,300)
print(lis)
lis.insert(19,100)
print(lis)

#extend functions appends multiple values at once 
lis.extend([300,400,500])
print(lis)


#how to remove any element from the lsit 
# by default pops last element as default is set to pop(-1)
lis.pop(-2)
print(lis)

lis.pop()
print(lis)


#remove function removes the first occured element in the list 

lis.append(2)
print(lis)
lis.remove(2)
print(lis)

#how to clear the list 
lis.clear()
print(lis)

#sorting a list
lis = [5,4,3,2,1]
print(lis)

lis.sort()
print(lis)

lis.clear()

#methods to copy and assign array values to another array , duplicate
lis =[1,2,3]
lis1 = lis
lis2 = lis.copy()
print(lis,lis1,lis2)
lis2[2] = 5
lis1[2] = 5
lis[2] = 5
print(lis,lis1,lis2)

#min max function
print(min(lis1))
print(max(lis1))
'''
from array import array 
arr = array('i',[10,20,30])
print(arr,type(arr))
arr.append(12.5)
print(arr)



