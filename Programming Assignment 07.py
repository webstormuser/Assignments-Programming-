#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to find sum of array?

# In[1]:


import logging


# In[2]:


import sys


# In[3]:


logging.basicConfig(filename="assignment7.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %('
                                                                          'message)s')
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s',
                              '%m-%d-%Y %H:%M:%S')
logger = logging.getLogger()
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)


# In[21]:


logging.info("Ouput of Finding sum of Array Elements")
def sum_Array():
    input_array=eval(input("Enter number"))
    logging.info(f'Entered numbers are{input_array}')
    logging.info(f'Sum of {input_array} is {sum(input_array)}')
    
sum_Array()


# 2. Write a Python Program to find largest element in an array?

# In[22]:


logging.info("Output of finding largest element in Array")
def largest():
    input_array=eval(input("Enter number"))
    logging.info(f'Entered Array is {input_array}')
    sorted_array=sorted(input_array,reverse=True)
    logging.info(f'sorted array in revered order is {sorted_array}')
    logging.info(f'Largest element in array is {sorted_array[0]}')
largest()


# 3. Write a Python Program for array rotation?

# In[29]:


#logging.info("output of rotation of array elements")
def rotateArray(arr,d,n):
    temp=[]
    i=0
    while(i<d):
        temp.append(arr[i])
        i=i+1
    i=0
    while(d<n):
        arr[i]=arr[d]
        i=i+1
        d=d+1
    arr[:]=arr[:i]+temp
    return arr
    
arr=[12,13,14,15,6,7,8,9]
logging.info(f"After rotation array is")
logging.info(rotateArray(arr,3,len(arr)))


# 4. Write a Python Program to Split the array and add the first part to the end?

# In[34]:


def SplitArr(arr,n,k):
    b=arr[:k]
    return arr[k::]+b[::]
arr=[12,13,14,15,16,17]
logging.info(f' Before Splitting the original array is {arr}')
n=len(arr)
k=3
logging.info(f'After spliting the array is {SplitArr(arr,n,k)}')


# 5. Write a Python Program to check if given array is Monotonic?

# In[ ]:


#monotonic means either its elements are continuously increasing or decresing 


# In[47]:


def isMonotonic(A):
       return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

A=[5,6,3,4]
logging.info(f'Enterred array is {A}')
logging.info(f' Array is monotonic {isMonotonic(A)}')
B=[3,4,5,6]
logging.info(f'Enterred array is {B}')
logging.info(f' Array is monotonic {isMonotonic(B)}')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




