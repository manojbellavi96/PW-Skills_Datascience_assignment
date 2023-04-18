#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1
marks=int(input("enter the marks scored : "))
if marks > 90:
 print("Grade secured='A'")
elif marks>80 and marks<=90:
 print("Grade secured='B'")
elif marks > 60 and marks <= 80:
 print("Grade secured='C'")
else:
 print("Grade secured='D'")


# In[ ]:


#2
cost_price=int(input("enter the cost price of the bike: "))
if cost_price> 100000:
    tax=cost_price*(15/100)
    print("Tax to be paid will be = ", tax)
elif cost_price> 50000 and cost_price<= 100000:
    tax = cost_price * (10 / 100)
    print("Tax to be paid will be = ", tax)
else:
    tax = cost_price * (5 / 100)
    print("Tax to be paid will be = ", tax)


# In[ ]:


#3
city=input("enter the city: ")
if city=="Delhi":
    print("monument found='Red Fort'")
elif city=='Agra':
    print("monument found='Taj Mahal'")
elif city=='Jaipur':
    print("monument found='Jal Mahal'")
else:
    print("no famous monument details available")


# In[ ]:


#4
num = int(input("enter the number: "))
if num>10:
 i = 0
 while num > 10:
    num = num//3
    i = i+1
    j = str(i)
 print("given number can be divided by " + j + " times")
else:
 print("unexpected input")


# In[1]:


#5
'''
It repeats a statement or multiple statements when a provided condition is True.
Before performing a loop body it check for a condition

Ex: 
 A child is learning to count number of 10 rupess in his hand 
and here we have given 5 notes of 10 rupess. 
Output will display the counting of notes and total amount

notes = 5
i=1 # starting number intialize
while i<=notes:
    print(i)
    i += 1
print('Total Money: ',notes*10,'Rupees')
'''


# In[ ]:


#6
'''
Pattern-1: 

n = int(input('Enter number of rows : '))
 
i = 1
while i <= n :
    j = 1
    while j <= i:
        print("*", end = " ")
        j += 1
    print()
    i += 1
    

Pattern-2:

n = int(input('Enter number of rows : '))
 
i = 1
while i <= n :
    j = n
    while j >= i:
        print("*", end = " ")
        j -= 1
    print()
    i += 1
    
Pattern-3:

n = int(input('Enter number of rows : '))
 
k = 1
i = 1
while i <= n :
    j = 1
    while j <= i:
        print("{:3d}".format(k), end = " ")
        j += 1
        k += 1
    print()
    i += 1
    
'''


# In[ ]:


#7
num=10
while num!=0:
    print(num)
    num=num-1


# In[ ]:


#8
i=10
for num in range(i):
    print(i)
    i=i-1

