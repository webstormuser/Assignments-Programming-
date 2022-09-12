#!/usr/bin/env python
# coding: utf-8

# # Question1. Write a function that stutters a word as if someone is struggling to read it. The
# first two letters are repeated twice with an ellipsis ... and space after each, and then the
# word is pronounced with a question mark ?.
# Examples
# stutter(&quot;incredible&quot;) ➞ &quot;in... in... incredible?&quot;
# stutter(&quot;enthusiastic&quot;) ➞ &quot;en... en... enthusiastic?&quot;
# stutter(&quot;outstanding&quot;) ➞ &quot;ou... ou... outstanding?&quot;
# 
# Hint :- Assume all input is in lower case and at least two characters long.

# In[1]:


def stutter(word):
    return (2*(word[:2]+'... '))+word+'?'
word="incredible"
stutter(word)


# # Question 2.
# Create a function that takes an angle in radians and returns the corresponding
# angle in degrees rounded to one decimal place.
# Examples
# radians_to_degrees(1) ➞ 57.3
# radians_to_degrees(20) ➞ 1145.9
# radians_to_degrees(50) ➞ 2864.8

# In[3]:


import math
def rad_to_degree(radians):
    print("Radians to degree:",(radians*(180/math.pi)))
    
radians=float(input("Enter radians value"))
rad_to_degree(radians) 


# # Question 3. 
# 
# In this challenge, establish if a given integer num is a Curzon number. If 1 plus
# 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon
# number.
# Given a non-negative integer num, implement a function that returns True if num is a Curzon
# number, or False otherwise.
# Examples
# is_curzon(5) ➞ True
# # 2 ** 5 + 1 = 33
# # 2 * 5 + 1 = 11
# # 33 is a multiple of 11
# is_curzon(10) ➞ False
# # 2 ** 10 + 1 = 1025
# # 2 * 10 + 1 = 21
# # 1025 is not a multiple of 21
# is_curzon(14) ➞ True
# # 2 ** 14 + 1 = 16385
# # 2 * 14 + 1 = 29
# # 16385 is a multiple of 29

# In[7]:


def Curzon(num):
    num1=2**num+1
    num2=2*num+1
    if num1%num2==0:
        print(num,"is a curzon")
    else:
        print(num,"is not a curzon")
for i in range(3):
    num=int(input("Enter a number"))
    Curzon(num)


# # Question 4.Given the side length x find the area of a hexagon.
# 
# 
# 
# Examples
# area_of_hexagon(1) ➞ 2.6
# area_of_hexagon(2) ➞ 10.4
# area_of_hexagon(3) ➞ 23.4
# 
# Question 5. Create a function that returns a base-2 (binary) representation of a base-10
# (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10)
# 010101001(2) = 1 + 8 + 32 + 128.
# Going from right to left, the value of the most right bit is 1, now from that every bit to the left
# will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).
# Examples
# binary(1) ➞ &quot;1&quot;
# # 1*1 = 1
# binary(5) ➞ &quot;101&quot;
# # 1*1 + 1*4 = 5
# binary(10) ➞ &quot;1010&quot;
# # 1*2 + 1*8 = 10

# In[8]:


def getBinary():
    in_num = int(input("Enter a Number: "))
    out_num = bin(in_num).replace('0b','') 
    print(f'Binary of {in_num} ➞ {out_num}')

for x in range(3):
    getBinary()


# In[ ]:




