#creating dictionarires

#Using curly braces ({})
my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
print(my_dict)
type(my_dict)

#using dict()
new_dict=dict()
print(new_dict)
type(new_dict)

#nested dictionary
emp_details={'Employee':{'Dave':{'ID':'001','Salary':'2000','Designation':'Team Lead'},
                         'Ava':{'ID':'002','Salary':'1500','Designation':'Associate'}}}
print(emp_details)


#Performing Operations on Hash tables using Dictionaries:
# 1. Accessing Items
my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
# Using key values
print(my_dict['Dave'])

# Using functions
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('Dave'))

# Implementing the for loop
my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
print("All keys")
for x in my_dict:
    print(x)       #prints the keys
print("All values")
for x in my_dict.values():
    print(x)       #prints values
print("All keys and values")
for x,y in my_dict.items():
    print(x, ":" , y)       #prints keys and values

# 2. Updating the dictionary
    
my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
my_dict['Dave'] = '004'   #Updating the value of Dave
my_dict['Chris'] = '005'  #adding a key-value pair
print(my_dict)

# 3 . Deleting elements from the dictionary

del my_dict['Dave']  #removes key-value pair of 'Dave'
my_dict.pop('Ava')   #removes the value of 'Ava'
my_dict.popitem()    #removes the last inserted item
print(my_dict)

# Converting Dictionary into a dataframe:

import pandas as pd
my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
df=pd.DataFrame(list(my_dict.items()),columns = ['Name','ID'])
print(df)

