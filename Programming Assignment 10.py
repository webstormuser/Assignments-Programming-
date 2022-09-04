#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to find sum of elements in list?
# 2.	Write a Python program to  Multiply all numbers in the list?
# 3.	Write a Python program to find smallest number in a list?
# 4.	Write a Python program to find largest number in a list?
# 5.	Write a Python program to find second largest number in a list?
# 6.	Write a Python program to find N largest elements from a list?
# 7.	Write a Python program to print even numbers in a list?
# 8.	Write a Python program to print odd numbers in a List?
# 9.	Write a Python program to Remove empty List from List?
# 10.	Write a Python program to Cloning or Copying a list?
# 11.	Write a Python program to Count occurrences of an element in a list?
# 

# In[43]:


def inputList(self):
        try:
            List1=[]
            while True:
                num=int(input("Enter number"))
                List1.append(num)
        except Exception as e:
            print(e)
        return List1
def Operations(self):
        List1=inputList() # calling input function for List 
        print(List1) #displaying input numbers from List
        print("**************Summation of all elements from List***********")
        sum1=0
        for i in List1:
            sum1=sum1+i
        print(f' Sum ---->{sum1}') # finding the sum of all elements into List
        print("**************Multiplication  of all elements from List***********")
        mult=1
        for i in List1:
            mult=mult*i
        print(f'multiplication-----> {mult}')
        print("***********************")
        largest=List1[0]
        for i in List1:
            if i>largest:
                largest=i
        print(f' largest element in list is-----> {largest}') # finding largest element from the List 
        print("*************************************")
        smallest=List1[0]
        for i in List1:
            if i<smallest:
                smallest=i
        print(f' smallest element in list is ------>{smallest}') # finding smallest number from list
        print("******************************")
        sortedList=sorted(List1,reverse=True)
        print("Second largest element from List is",sortedList[1])    
l=ListOperations()
l.Operations()


# In[46]:


def nLargestEleInList(k):
    in_ele = int(input('Enter the No of elements in a list: '))
    in_list = []
    for ele in range(in_ele):
            in_list.append(int(input('Enter a Element: ')))
    print(f'The {k} Largest Element in {in_list} is {sorted(in_list, reverse=True)[0:k]}')

nLargestEleInList(4)


# # Write a Python program to print even numbers in a list?

# In[48]:


def evenNoInList():
    in_ele = int(input('Enter the No of elements in a list: '))
    in_list = []
    even_list = []
    for ele in range(in_ele):
        in_list.append(int(input('Enter a Element: ')))
    for ele in in_list:
        if ele%2 == 0:
            even_list.append(ele)
    print(f'The Even Elements in {in_list} are {even_list}')

evenNoInList()


# # Write a Python program to print odd numbers in a list?

# In[51]:


def oddNoInList():
    in_ele = int(input('Enter the No of elements in a list: '))
    in_list = []
    odd_list = []
    for ele in range(in_ele):
        in_list.append(int(input('Enter a Element: ')))
    for ele in in_list:
        if ele%2 == 1:
            odd_list.append(ele)
    print(f'The Odd Elements in {in_list} are {odd_list}')

oddNoInList()


# # Write a Python program to Remove empty List from List?

# In[66]:


def checkEmptyList(List1):
    NewList=[]
    for ele in List1:
        if ele:
            NewList.append(ele)
    print(f'After removing empty list {NewList}')
List1=[1,2,3,4,5,[],[]]   
print(f' Original list is {List1}')
checkEmptyList(List1)


# # Write a Python program to Cloning or Copying a list?

# In[78]:


def CloneList(List1):
    #Method one
    List2=List1[:]
    print(f' After cloning list is {List2}')
    #method two
    List3=[]
    List3=List1.copy()
    print(f' After cloning using other method list is {List3}')
    
List1=[1,3,4,5,78,90]
CloneList(List1)


# In[ ]:





# # Write a Python program to Count occurrences of an element in a list?

# In[77]:


def checkOccurence():
    in_list = eval(input('Enter the elements of the list: '))
    in_num = eval(input('Enter the element to find: '))
    count = 0
    if in_num in in_list:
        for ele in in_list:
            if ele == in_num:
                count = count+1
    print(f'There are {count} occurences of {in_num} in {in_list}')
    
checkOccurence()


# 
