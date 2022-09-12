#!/usr/bin/env python
# coding: utf-8

# 1.Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example: Let us assume the following comma separated input sequence is given to the program:100,150,180
# The output of the program should be: 18,22,24

# In[7]:


from math import sqrt
def calculate():
    #define and set values for C,H 
    C=50
    H=30
    D=eval(input("Enter number"))
    output=[]
    for i in D:
        Q=str(int(sqrt((2*C*i)/H)))
        output.append(Q)
    print("The output of program {}".format(','.join(output)))
calculate()


# 2.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡Y-1.
# Example: Suppose the following inputs are given to the program: 3,5
# Then, the output of the program should be:[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# In[9]:


import array as arr
def GenerateArray():
    X=int(input("Enter no of rows"))
    Y=int(input("Enter no of columns"))
    output=[]
    for ele in range(X):
        output.insert(X,[])
        for sub_ele in range(Y):
            output[ele].append(ele*sub_ele)
    print(output)
GenerateArray()


# 3.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically ?
# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

# In[14]:


def sortWords():
    in_put=input("Enter a sequence of words separated by comma")
    words=[word for word in in_put.split(',')]
    result=','.join(sorted(words))
    print(words)
    print(result)
sortWords()


# 4.Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again
# Then, the output should be: again and hello makes perfect practice world

# In[20]:


def removeDuplicates():
    in_put=input("Enter a sequence of words separated by comma")
    words=[word for word in in_put.split(' ')]
    result=' '.join(sorted(sorted(list(set(words)))))
    print(words)
    print(result)
removeDuplicates() 


# 5.Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program: hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# In[22]:


def calnoletter():
    in_put=input("Enter a string containing combination of letters and numbers")
    print("Orinal string is ",in_put)
    letter=0
    no=0
    for ele in in_put:
        if ele.isdigit():
            no=no+1
        if ele.isalpha():
            letter=letter+1
    print("LETTERS",letter,end=" \n")
    print("DIGITS",no)
calnoletter()    


# 6.A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 
# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# 
# Example:
# If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:ABd1234@1

# In[25]:


def checkPass():
    small="abcdefghijklmnopqrstuvwxyz"
    capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    no="0123456789"
    symbol="$#@"
    in_string=input("Enter the string of password")
    for ele in in_string.split(","):
        if len(ele) <= 12 and len(ele) >=6 :
            if any(i.isupper() for i in ele):
                if any(i.islower() for i in ele):
                    if any(i for i in ele if i in symbol):
                        print(ele)
checkPass()


# In[ ]:




