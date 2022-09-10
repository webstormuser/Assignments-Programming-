#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to find words which are greater than given length k?
# 2.	Write a Python program for removing i-th character from a string?
# 3.	Write a Python program to split and join a string?
# 4.	Write a Python to check if a given string is binary string or not?
# 5.	Write a Python program to find uncommon words from two Strings?
# 6.	Write a Python to find all duplicate characters in string?
# 7.	Write a Python Program to check if a string contains any special character?
# 

# In[81]:


# Write a Python program to find words which are greater than given length k?
def checkLengthOfString():
    in_String=input("Enter String")
    in_Length=int(input("Enter length of string"))
    outputString=[]
    for string in in_String.split(" "):
        if len(string)>in_Length:
            outputString.append(string)
    print(','.join(outputString))
checkLengthOfString()            


# In[ ]:


#Write a Python program for removing i-th character from a string?


# In[5]:


def removeIthchar():
    out_String=''
    input_String=input("Enter String")
    input_Char_no=int(input("Enter ith Character"))
    for ele in range(len(input_String)):
        if ele != input_Char_no:
            out_String=out_String+input_String[ele]
    print(out_String)
removeIthchar()


# In[9]:


#Write a python program to split and join a string 

def split_join():
    in_string=input("Enter String")
    out_string=" "
    print(f"Splitted String is {in_string.split(' ')}")
    print(f" After Splitting and join string is {','.join(in_string.split(' '))}")
split_join()


# In[16]:


#Write a Python to check if a given string is binary string or not?
def checkBinary():
    flag=0
    string=input("Enter String")
    for ele in string:
        if ele in ['0','1']:
            flag=1
            continue
        else:
            flag=0
            break
    statement='it is bianry string' if flag==1 else "It is not binary string"
    print(f"{string} {statement}")
checkBinary()
checkBinary()


# In[18]:


#Write a python program to find uncommon wordds from two string 
def find_uncommon_words():
    string1=input("Enter String")
    string2=input("Enter String")
    strList1=string1.split()
    strList2=string2.split()
    uncommonwords=' '
    for words in strList1 :
        if words not in strList2:
            uncommonwords =uncommonwords+" "+words
    for words in strList2 :
        if words not in strList1:
            uncommonwords =uncommonwords+" "+words
    print("All uncommon words are", uncommonwords)
find_uncommon_words()


# In[19]:


#Write  a python program to find all duplicate characters in a string 
def duplicateChars():
    in_string = input('Enter the string: ')
    non_duplicate_list = []
    duplicate_list = []
    for ele in in_string:
        if ele not in non_duplicate_list:
            non_duplicate_list.append(ele)
        else:
            duplicate_list.append(ele)
    print(f'Duplicate characters are: {list(set(duplicate_list))}')
        
duplicateChars()


# In[23]:


#Write a python prgoram to check string contain any special character
def chk_spl_symbol():
    symbols='[@_!#$%^&*()<>?/\|}{~:]'
    char_list=[]
    count=0
    in_string=input("Enter String")
    for ele in in_string:
             if ele in symbols:
                char_list.append(ele)
                count=count+1
    print(f" There are {count} special characters symbols in {in_string} they are {char_list}")  
chk_spl_symbol()


# In[ ]:




