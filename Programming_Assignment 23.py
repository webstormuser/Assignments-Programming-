#!/usr/bin/env python
# coding: utf-8

# # Question 1
# Create a function that takes a number as an argument and returns True or False depending
# on whether the number is symmetrical or not. A number is symmetrical when it is the same as
# its reverse.
# Examples
# is_symmetrical(7227) ➞ True
# is_symmetrical(12567) ➞ False
# is_symmetrical(44444444) ➞ True
# is_symmetrical(9939) ➞ False
# is_symmetrical(1112111) ➞ True

# In[1]:


def is_symmetrical(in_num):
    if str(in_num) == str(in_num)[::-1]:
        print(f'{in_num} ➞ {True}')
    else:
        print(f'{in_num} ➞ {False}')

is_symmetrical(7227)
is_symmetrical(12567)
is_symmetrical(44444444)
is_symmetrical(9939)
is_symmetrical(1112111)


# # Question 2
# Given a string of numbers separated by a comma and space, return the product of the
# numbers.
# Examples
# multiply_nums(&quot;2, 3&quot;) ➞ 6
# multiply_nums(&quot;1, 2, 3, 4&quot;) ➞ 24
# multiply_nums(&quot;54, 75, 453, 0&quot;) ➞ 0
# multiply_nums(&quot;10, -2&quot;) ➞ -20

# In[6]:


def mutiply_num(lst):
    out_result=1
    out_string=lst.replace(" ","").split(",")
    for ele in out_string:
        out_result=out_result*int(ele)
    print(f"{lst}-->{out_result}")
mutiply_num("2,3")


# # Question 3
# Create a function that squares every digit of a number.
# Examples
# square_digits(9119) ➞ 811181
# square_digits(2483) ➞ 416649
# square_digits(3212) ➞ 9414
# Notes
# The function receives an integer and must return an integer.

# In[8]:


def sqaure_digits(num):
    in_list=[str(int(ele)**2)for ele in str(num)]
    out_list="".join(in_list)
    print(f"{num}--->{out_list}")
sqaure_digits(9119)


# # Question 4
# Create a function that sorts a list and removes all duplicate items from it.
# Examples
# setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]
# setify([4, 4, 4, 4]) ➞ [4]
# setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]
# setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]

# In[15]:


def setify(lst):
    try:
        sort_list=sorted(lst)
        print(f"sorted list-->{sort_list}")
        out_list=[]
        for ele in sort_list:
            if ele not in out_list:
                out_list.append(ele)
        print(f"After removing duplicates-->{out_list}")
    except Exception as e:
        print(e)
setify([3,3,3,2,1])
setify([1,3,3,5,5])
setify([5,7,8,9,10,15])
setify([4,4,4,4])


# # Question 5
# Create a function that returns the mean of all digits.
# Examples
# mean(42) ➞ 3
# mean(12345) ➞ 3
# mean(666) ➞ 6
# Notes
#  The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in
# 512 is (5+1+2)/3(number of digits) = 8/3=2).
#  The mean will always be an integer.

# In[24]:


def mean(num):
    in_list=[int(ele)for ele in str(num)]
    out_mean=sum(in_list)/len(str(num))
    print(f"{num}--->{out_mean:.0f}")
mean(42)
mean(666)
mean(12345)
mean(2345)


# In[ ]:




