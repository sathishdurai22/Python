#!/usr/bin/env python
# coding: utf-8

# # 1)Manipulate using a list:
#     1.to add new elements to the end of the list.
#     2.to reverse element in the list.
#     3.to display the same list of the elements multiple times.
#     4.to concatenate two list.
#     5.to sort the elemnts in the list in ascending order.

# In[1]:


ls=[22,10,11,5]
ls


# In[3]:


#1) to add new elements to the end of the list.
ls.append(100) # append is used to add single element at the end of the list.

#to add multiple elements -extend
ls.extend([25,35,200])

print('after added list elements are: ',ls)


# In[4]:


#2) to reverse element in the list.
ls.reverse()

print('reversed list is: ',ls)


# In[5]:


#3)to display the same list of the elements multiple times.

ls=[200,35,25,100,200,35,25,100,5,11,10,22] * 3

print('the elements printed multiple times: ',ls)


# In[8]:


#4)to concatenate two list.
ls1=[22,10,11,5]
ls2=[20,30,42]

con=ls1 + ls2

print ('after concatenate my two list: ',con)


# In[12]:


#5.to sort the elemnts in the list in ascending order.

con.sort()

print('after sort in ascending order: ',con)


# # 2)Write a python program to do in the tuples.
# 1)manipulate using tuples.
# 2)to add new elemnts to the end of the tuples.
# 3)to reverse elements in the list.
# 4)to display the elements of the same tuples multiple times.
# 5)to concatenate two tuples.
# 6)to sort the elements in the list in ascending order.

# In[13]:


#1)manipulate using tuples.
tu=(1,5,6,'abc',50,20)
tu


# In[35]:


#2)to add new elemnts to the end of the tuples.
tu2=('spark',100)
tu1=(26,'cd',99)
tuple=tu1 + tu2
print('after add a new element:',tuple)


# In[39]:


#3)to reverse elements in the list.
tuple=([26, 'cd', 99, 'spark', 100])

tuple.reverse()

print('reverse element:',tuple)


# In[ ]:


#4)to display the elements of the same tuples multiple times.
tuple=(26, 'cd', 99, 'spark', 100) * 5

print(tuple)


# In[41]:


#5)to concatenate two tuples.
tuple1=(26, 'cd', 99, 'spark', 100)
tuple2=(60,44,'bell',2,100)

tuple =tuple1+tuple2

print(tuple)


# In[54]:


#6)to sort the elements in the list in ascending order.
vowels=['e','a','u','o','i']
vowels.sort()
print(vowels)


# # 3)write a python program to implement the following using list
# 

# In[57]:


#1)create a list with integers(min 10 numbers)

lst=[2,5,66,28,45,63,10,1,9,22]


# In[59]:


#2)display lats number in the list
lst[-1:]


# In[60]:


#3)display the value from the list[0:4]

lst[0:4]


# In[62]:


#4)display the value from the list[2:]

lst[2:]


# In[63]:


#5)display the value from the list[:6]
lst[:6]


# # 4.write a python program:
# tuple=(10,50,20,40,30)

# In[68]:


#1)display the element 10 and 50 from tuple1

tuple1=(10,50,20,40,30)

tuple1[0:2]


# In[69]:


#2)display the length of tuple1.

len(tuple1)


# In[70]:


#3)to find minimum element from tuple1

min(tuple1)


# In[71]:


#4)to add all element in the tuple1. 

sum(tuple1)


# In[74]:


#5)to display the same tuple1  multiple times.
tuple=tuple1 * 10
print(tuple)


# # 5)write python program:

# In[75]:


#1)to calculate the length of string
string='Hello welcome to mphasis'

len(string)


# In[77]:


#2)to reverse words in a string

string[::-1]


# In[80]:


#3)to display the same string multiple times

str= string * 5

print(str)


# In[82]:


#4)to concatenate two strings
str1='we are vitians'
a=string +" " +str1
print(a)


# In[87]:


#5)str1="South India",using string slicing to display"India"
str1='South India'
str1[6:11]


# In[ ]:


# 6)perform the following:
# 1)creating the dictionary
person={'f_name':'durai','l_name':'k','age':24,'city':'arani'}
print("person: ",person)


# In[97]:


#2)accessing values and keys in dictionary.

person.values()


# In[98]:


person.keys()


# In[100]:


#3)updating the dictionary using a function.
person.update({'f_name':'Durairaj'})
print(person)


# In[101]:


#4)clear and delete the dictionary values.
person.clear() #clear the inside key and values
print(person)

# del person['city'] use this command and the directories


# In[ ]:


#7)python program to insert a number to any position in a list
list = ['to','vit']
list.insert(0, 'Welcome')
print(list)


# In[110]:


#8)python program to delete  an element  from a list by index.
list = [5, 6, 3, 7, 8, 1, 2, 10, 5]
del list[4]
print(list)


# In[117]:


#9)write a program to display a number from 1 to 100.
a=100
i=0
while i<a:
    i=i+1
    print (i)


# In[130]:


#10)Write a python program to find the sum of all items in a tuple.
tuple=(5,6,5,6,1)
sum(list)


# In[ ]:


#11)


# In[137]:


#12)A list of words is given.Find the words from the list that have their second character in uppercase.
ls=['hello','Dear','hOw','ARe','You']
list=[]
for word in ls:
    if len(word)>=3 and word[1].isupper():
        list.append(word)
print(list)


# In[ ]:


#13)


# # Control Structure
# # 1)Write a python program to find N prime number
# 

# In[143]:


num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


# # 2)Write the python code that calculates the salary of an employee.prompt the user to enter basic salary,HRA,TA,and DA.Add these components to calculate the gross Salary.Also,deduct 10% of salary from the gross Salary to be paid as tax and display gross minus tax as net salary.

# In[157]:


basic_salary = float(input("Enter Basic Salary: "))
hra = float(input("Enter HRA: "))
ta = float(input("Enter TA: "))
da = float(input("Enter DA: "))

# Calculate gross salary
gross_salary = basic_salary + hra + ta + da

# Calculate tax amount (10% of gross salary)
tax = 0.10 * gross_salary

# Calculate net salary (gross salary - tax)
net_salary = gross_salary - tax

# Display the results
print(f"Gross Salary: {gross_salary:.2f}")
print(f"Tax Deducted: {tax:.2f}")
print(f"Net Salary: {net_salary:.2f}")


# # 3)write a python program to search for a string in the given list

# In[162]:


# Sample list of strings
my_list = ["welcome", "to", "mphasis","Dream","big"]

# String to search for
search_string = input("Enter the string to search for: ")

# Initialize a flag to check if the string is found
found = False

# Iterate through the list and check if the string exists
for item in my_list:
    if search_string.lower() == item.lower():
        found = True
        break

# Check the result and display a message
if found:
    print(f"The string '{search_string}' was found in the list.")
else:
    print(f"The string '{search_string}' was not found in the list.")



# In[ ]:





# In[ ]:




