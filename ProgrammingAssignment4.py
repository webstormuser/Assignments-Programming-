#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to Find the Factorial of a Number?
# 2. Write a Python Program to Display the multiplication Table?
# 3. Write a Python Program to Print the Fibonacci sequence?
# 4. Write a Python Program to Check Armstrong Number?
# 5. Write a Python Program to Find Armstrong Number in an Interval?
# 6. Write a Python Program to Find the Sum of Natural Numbers?

# In[14]:


def fact(num):
    if num <1 :
        return 1
    else :
        return num*fact(num-1)
num=int(input('Enter number'))
value=fact(num)
print("Factorial is ",value)


# In[19]:


def mult_table(num):
    for i in range(1,11):
        print(num,'*',i,"=",num*i)
num=int(input("Enter number"))
table=mult_table(num)


# In[30]:


def fibo(num):
    start=[0,1]
    if num<0:
        print("Series cnt be negative")
    elif num >=0 and num <=2:
        print(start)
    else :
        for i in range (num):
            if i >=2:
                start.append(start[i-1]+start[i-2])
        print(start)


# In[31]:


fibo(5)


# In[41]:


def armstrong(num):
    sum1=0
    temp=num
    while temp>0:
        r=temp%10
        sum1=sum1+r**3
        temp=temp//10
    if sum1==num:
        print("number is armstrong")
    else :
        print("Number is not armstrong")
num=int(input("Enter number"))
armstrong(num)


# In[54]:


def checkArmstrongNumber(in_num, storage):
    sum = 0
    for char in range(len(in_num)):
        sum = sum + pow(int(in_num[char]),3)
    if sum == int(in_num):
        storage.append(int(in_num))

start_interval = int(input('Enter the Start of the Interval: '))
end_interval = int(input('Enter the End of the Interval: '))
list_of_armstrong = []

if start_interval > end_interval:
    print("Start Interval Cannot be Greater than End Interval")
else:
    for number in range(start_interval,end_interval+1):
        checkArmstrongNumber(str(number),list_of_armstrong)
    print(f'The Armstrong numbers between {start_interval} and {end_interval} are {list_of_armstrong}')


# In[55]:


def sumOfNaturalNumbers(num):
    sum = num*((num+1)/2)
    print(f'Sum of {num} natural numbers is {sum}')
    
num = int(input('Enter a number: '))
sumOfNaturalNumbers(num)


# In[ ]:




