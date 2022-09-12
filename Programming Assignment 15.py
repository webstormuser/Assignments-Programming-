#!/usr/bin/env python
# coding: utf-8

# # Question 1:
# Please write a program using generator to print the numbers which can be divisible by 5 and
# 7 between 0 and n in comma separated form while n is input by console.
# Example:
# If the following n is given as input to the program:
# 100
# Then, the output of the program should be:
# 0,35,70

# In[10]:


class Generator:
    def __init__(self,num):
        self.num=num
    def gerateNum(self):
        for i in range(0,self.num+1):
            if i%5==0 and i%7==0:
                yield i
g=Generator(100)
for num in g.gerateNum():
    print(num,end=",")


# # Question 2:
# Please write a program using generator to print the even numbers between 0 and n in comma
# separated form while n is input by console.
# Example:
# If the following n is given as input to the program:
# 10
# Then, the output of the program should be:
# 0,2,4,6,8,10

# In[12]:


class Generator:
    def __init__(self,num):
        self.num=num
    def gerateNum(self):
        for i in range(0,self.num+1):
            if i%2==0:
                yield i
g=Generator(30)
for num in g.gerateNum():
    print(num,end=",")


# # Question 3:
# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n&gt;1
# Please write a program using list comprehension to print the Fibonacci Sequence in comma
# separated form with a given n input by console.
# Example:
# If the following n is given as input to the program:
# 7
# 
# Then, the output of the program should be:
# 0,1,1,2,3,5,8,13

# In[15]:


def generateFibo(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    elif num>1:
        return generateFibo(num-1)+generateFibo(num-2)
print([generateFibo(x)for x in range(20)])


# # Question 4:
# Assuming that we have some email addresses in the &quot;username@companyname.com&quot; format,
# please write program to print the user name of a given email address. Both user names and
# company names are composed of letters only.
# Example:
# If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# john

# In[21]:


def genEmail():
    email=input("Enter valid email address")
    out_name=email.split("@")[0]
    print("the usernames are :",out_name)
for i in range(3):
    genEmail()


# # Question 5:
# Define a class named Shape and its subclass Square. The Square class has an init function
# which takes a length as argument. Both classes have a area function which can print the area
# of the shape where Shape&#39;s area is 0 by default.

# In[22]:


class Shape :
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length*self.length
Sq=Square(15)
print("Area of square is ",Sq.area())


# In[ ]:




