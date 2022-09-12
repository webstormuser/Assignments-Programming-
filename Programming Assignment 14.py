#!/usr/bin/env python
# coding: utf-8

# # Question 1:
# Define a class with a generator which can iterate the numbers, which are divisible by
# 7, between a given range 0 and n.

# In[33]:


class Generator:
    def __init__(self,num):
        self.num=num
    def gerateNumber(self):
        for ele in range(0,self.num+1):
            if ele%7==0:
                yield ele
g=Generator(400)
for i in g.gerateNumber():
    print(i,end=' ')


# # Question 2:
# Write a program to compute the frequency of the words from the input. The output
# should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or
# Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# In[38]:


def checkFrequency():
    in_string=input("Enter string to check frquency")
    frquency={}
    for ele in in_string.split(" "):
        if frquency.get(ele)==None:
            frquency[ele]=1
        else:
            frquency[ele]+=1
    for ele in sorted(frquency):
        print(f'{ele}:{frquency[ele]}',end=" ")
checkFrequency()


# # Question 3:
# 
# Define a class Person and its two child classes: Male and Female. All classes have a
# method &quot;getGender&quot; and Male class print male and female class print female

# In[39]:


class Person():
    def getGender():
        pass
    
class Male(Person):
    def getGender():
        print("Male")
        
class Female(Person):
    def getGender():
        print("Female")

Male.getGender()
Female.getGender()


# # Question 4:
# Please write a program to generate all sentences where subject is in [&quot;I&quot;, &quot;You&quot;] and
# verb is in [&quot;Play&quot;, &quot;Love&quot;] and the object is in [&quot;Hockey&quot;,&quot;Football&quot;].

# In[40]:


def generateSentence():
    subject=["I","You"]
    verb=["Play","Love"]
    object=["Hockey","Football"]
    for s in subject:
        for v in verb:
            for o in object:
                print(f" {s} {v} {o}")
generateSentence()


# # Question 5:
# Please write a program to compress and decompress the string &quot;hello world!hello
# world!hello world!hello world!&quot;.

# In[51]:


import zlib
import gzip
import sys
def compdecomp():
    text=b'hello world!hello world!hello world!hello world!'
    print("original text is",text)
    print("Orinal text size is",sys.getsizeof(text))
    comp=zlib.compress(text)
    print("After compressing text is",comp)
    print("After compressing text size is ",sys.getsizeof(comp))
    decomp=zlib.decompress(comp)
    print("Decompressed text is ",decomp)
    print("After decompressed size of text is ",sys.getsizeof(decomp))
compdecomp()


# # Question 6:
# Please write a binary search function which searches an item in a sorted list. The
# function should return the index of element to be searched in the list.

# In[60]:


sorted_list = [1,2,3,4,5,6,7,8,9,10]
def binary_search(in_list,in_num):
    low = 0
    high = len(in_list)-1
    while low <= high:
        mid = high+low//2
        if in_list[mid] < in_num:
            low = mid+1
        elif in_list[mid] > in_num:
            high = mid-1
        else:
            return mid
    else:
        return 'Input Element not in the list'
    
print(binary_search(sorted_list,8))
print(binary_search(sorted_list,100))


# In[ ]:





# In[ ]:





# In[ ]:




