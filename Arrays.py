'''Arrays are a fundamental data structure, and an important part of most programming languages. In Python, they are containers which are 
able to store more than one item at the same time.
Specifically, they are an ordered collection of elements with every value being of the same data type. That is the most important thing 
to remember about Python arrays - the fact that they can only hold a sequence of multiple items that are of the same type.
Arrays are a fundamental data structure, and an important part of most programming languages. In Python, they are containers which are 
able to store more than one item at the same time.
Specifically, they are an ordered collection of elements with every value being of the same data type. That is the most important thing
 to remember about Python arrays - the fact that they can only hold a sequence of multiple items that are of the same type.'''

 '''What's the Difference between Python Lists and Python Arrays?
 
 Lists store items that are of various data types. This means that a list can contain integers, floating point numbers, strings, or any
other Python data type, at the same time. That is not the case with arrays.
As mentioned in the section above, arrays store only items that are of the same single data type. There are arrays that contain only 
integers, or only floating point numbers, or only any other Python data type you want to use.'''



#Creating a array

import array as arr
arr.array()
#or
from array import *
array()

#Defining a array
#variable_name = array(typecode,[elements])
'''variable_name would be the name of the array.
The typecode specifies what kind of elements would be stored in the array. Whether it would be an array of integers, an array of floats or an array of any other Python data type. Remember that all elements should be of the same data type.
Inside square brackets you mention the elements that would be stored in the array, with each element being separated by a comma. You can also create an empty array by just writing variable_name = array(typecode) alone, without any elements.'''

import array as arr 
numbers = arr.array('i',[10,20,30])
print(numbers)

#finding length
print(len(numbers))

#Indexing
print(numbers[0])
print(numbers[-1])

#Searching
print(numbers.index(10))

#Loop
for number in numbers:
    print(number)
#or
for value in range(len(numbers)):
    print(numbers[value])

#Slice
print(numbers[:2])  #first to second position
print(numbers[1:3]) #second to third position

#Changing val
#change it from having a value of 10 to having a value of 40
numbers[0] = 40
print(numbers)

#Adding with append()
#add the integer 40 to the end of numbers
numbers.append(40)
print(numbers)
#extend()
numbers.extend([40,50,60])
print(numbers)
#insert()
numbers.insert(0,40) #takes index and val to be inserted
print(numbers)

#Remove
numbers.remove(50)
print(numbers)
#pop
numbers.pop(2) #takes index value




