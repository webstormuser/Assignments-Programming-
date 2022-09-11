#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to Extract Unique values dictionary values?
# 2. Write a Python program to find the sum of all items in a dictionary?
# 3. Write a Python program to Merging two Dictionaries?
# 4. Write a Python program to convert key-values list to flat dictionary?
# 5. Write a Python program to insertion at the beginning in OrderedDict?
# 6. Write a Python program to check order of character in string using OrderedDict()?
# 7. Write a Python program to sort Python Dictionaries by Key or Value?

# 1. Write a Python program to Extract Unique values dictionary values?

# In[1]:


def unique_Dict():
    in_dict={
        "math":[90,90,86,85,83],
        "science":[67,67,89,90,88],
        "history":[67,78,97,77,78]
    }
    print(f" Original dictinory is : {in_dict.values()}")
    res=[]
    for sub in in_dict:
        for marks in in_dict[sub]:
            if marks not in res:
                res.append(marks)
    print(f" unique values from dict values are :{res}")
            
unique_Dict()


# In[2]:


#Write a Python program to find the sum of all items in a dictionary?
def sum_all_items():
    in_dict={
        "math":[90,90,86,85,83],
        "science":[67,67,89,90,88],
        "history":[67,78,97,77,78]
    }
    total=0
    print(f" Original dictinory is : {in_dict.values()}")
    for num in in_dict.values():
        if type(num)==list:
            for ele in range(len(num)):
                total=total+num[ele]
    print(f" Total of all elements from dictionary is {total}")                
sum_all_items()


# In[3]:


#Write a Python program to Merging two Dictionaries?
def merge_dict():
    emplolyee={}
    dept={}
    for i in range(3):
        name =input("Enter name")
        age=int(input("Enter age"))
        emplolyee[name]=age
        deptnm=input("Enter department name")
        loc=input("enter location")
        dept[deptnm]=loc
    print(f" First Dictionary -->{emplolyee}")
    print(f" Second Dictionary -->{dept}")
    result={**emplolyee,**dept}
    print(f" After merging two dictionaries-->{result}")
merge_dict()


# In[4]:


course_details = {
    'cousre_name':'Ineuron'
}
instructors = {
    'course_instructors':['Sudhanshu Kumar','Krish Naik']
}
course_details.update(instructors)
print(course_details)


# In[5]:


#Write a Python program to convert key-values list to flat dictionary?
in_list = [('A',10),('B',20),('C',30),('D',40),('E',50),('F',60),('G',70),('H',80),('I',90),('J',100)]
#method 1
out_dict=dict(in_list)
print(out_dict)
#method 2
out_dict1={}
for ele in in_list:
    out_dict1[ele[0]]=ele[1]
print(out_dict1)


# In[6]:


#Write a Python program to insertion at the beginning in OrderedDict?
#To insert at begining in OrderedDict move_to_end() and last =False is set
from collections import OrderedDict
dict_one=OrderedDict({"Apple":"iPhone","Google":"Chrome","Microsoft":"Windows"})
print(f" Original Dictionary is {dict_one}")
dict_two={"Tesla":"SpaceX"}
dict_one.update(dict_two)
print(dict_one)

'''To insert second dictionary content at begining move_to_end() is used'''
dict_one.move_to_end('Tesla',last=False)
print(f" After inserting at start {dict_one}")


# In[7]:


#Write a Python program to check order of character in string using OrderedDict()?
from collections import OrderedDict 
  
def checkOrder(input, pattern): 
      
    # create empty OrderedDict 
    # output will be like {'a': None,'b': None, 'c': None} 
    dict = OrderedDict.fromkeys(input) 
  
    # traverse generated OrderedDict parallel with 
    # pattern string to check if order of characters 
    # are same or not 
    ptrlen = 0
    for key,value in dict.items(): 
        if (key == pattern[ptrlen]): 
            ptrlen = ptrlen + 1
          
        # check if we have traverse complete 
        # pattern string 
        if (ptrlen == (len(pattern))): 
            return 'true'
  
    # if we come out from for loop that means 
    # order was mismatched 
    return 'false'
  
# Driver program 
if __name__ == "__main__": 
    input = 'engineers rock'
    pattern = 'er'
    print (checkOrder(input,pattern)) 


# In[16]:


#Write a Python program to sort Python Dictionaries by Key or Value?
dict_one={"Data Science":17700,"Data Analyst":4800,"Full Stack Developer":4800,"Python Developer":7700}
def sort_Dict(dict_one,sort_type):
    if sort_type == 'key':
        print(dict(sorted(dict_one.items(), key=lambda x:x[0], reverse=False)))
    else:
        print(dict(sorted(dict_one.items(), key=lambda x:x[1], reverse=False)))        
sort_Dict(dict_one,'key')        
sort_Dict(dict_one,'value')


# In[ ]:




