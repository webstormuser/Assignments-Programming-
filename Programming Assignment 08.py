#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import logging


# In[2]:


logging.basicConfig(filename="assignment.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %('
                                                                          'message)s')
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s',
                              '%m-%d-%Y %H:%M:%S')
logger = logging.getLogger()
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)


# # 1. Write a Python Program to Add Two Matrices?

# In[20]:


matrix1=[]
matrix2=[]
result=[]
row=int(input("Enter no of rows"))
print("Enter elements into first matrix")
for i in range(row):
    rows=[]
    for j in range(row):
        rows.append(int(input()))
    matrix1.append(rows)
print("Enter elements into second matrix")
for i in range(row):
    rows=[]
    for j in range(row):
        rows.append(int(input()))
    matrix2.append(rows)
logging.info(matrix1)
logging.info(matrix2)

print("addition reuslt is")
for i in range(row):
    rows=[]
    for j in range(row):
        rows.append(matrix1[i][j]+matrix2[i][j])
    result.append(rows)
logging.info(result)


# # 2. Write a Python Program to Multiply Two Matrices?

# In[28]:


def Multiply(A,B):
    result=[ [0,0,0],[0,0,0],[0,0,0] ]
    #for rows
    for i in range(len(A)):
        #for columns
        for j in range(len(B[0])):
            #for rows of matrix B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    for p in result:
        logging.info(p)

    return 0

A = [ [1, 2, 3],[6, 7, 4], [8, 10, 11] ]
  
B = [[1, 5, 3],[2, 6, 5], [7, 4, 9] ]

logging.info(f" Multiplcation Result: ")
Multiply(A,B)


# # 3. Write a Python Program to Transpose a Matrix?

# In[30]:


a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,2],[4,5],[7,8]]
c = [[1,2,3],[4,5,6]]

def generate_transpose(in_matrix):
    out_matrix = []
    for ele in range(len(in_matrix[0])):
        out_matrix.append([0 for i in range(len(in_matrix))])
    for i in range(len(in_matrix)):
        for j in range(len(in_matrix[i])):
            out_matrix[j][i] = in_matrix[i][j]
    print(f'{in_matrix} -> {out_matrix}')
        
generate_transpose(a)
generate_transpose(b)
generate_transpose(c)


# # 4. Write a Python Program to Sort Words in Alphabetic Order?

# In[57]:


def sortString():
    string=input("Enter String ").title()
    logging.info(f'original string is{string}')
    sortString =sorted(string.split(" "))
    print(' '.join(sortString))
sortString()


# # 5. Write a Python Program to Remove Punctuation From a String?

# In[61]:


# define punctuation
def removePunctuation():
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    my_str = input("Enter your string")
 #   "Hello!!!, he said ---and went."
    
    # remove punctuation from the string
    no_punct = ""
    for char in my_str:
           if char not in punctuations:
                   no_punct = no_punct + char

# display the unpunctuated string
    print(no_punct)
    
removePunctuation()


# In[ ]:




