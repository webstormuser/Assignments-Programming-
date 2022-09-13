#!/usr/bin/env python
# coding: utf-8

# Question1. Create a function that takes three arguments a, b, c and returns the sum of the
# numbers that are evenly divided by c from the range a, b inclusive.
# Examples
# evenly_divisible(1, 10, 20) ➞ 0
#  No number between 1 and 10 can be evenly divided by 20.
# evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30
# evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18

# In[2]:


def evenDivisible(a,b,c):
    Num_List=[]
    for num in range(a,b+1):
        if num%c==0:
            Num_List.append(num)
    print(f'{a,b,c}-->{sum(Num_List)}')
evenDivisible(1,10,20)
evenDivisible(1,10,2)
evenDivisible(1,10,3)


# Question2. Create a function that returns True if a given inequality expression is correct and
# False otherwise.
# Examples
# correct_signs(&quot;3 &lt; 7 &lt; 11&quot;) ➞ True
# correct_signs(&quot;13 &gt; 44 &gt; 33 &gt; 1&quot;) ➞ False
# correct_signs(&quot;1 &lt; 2 &lt; 6 &lt; 9 &gt; 3&quot;) ➞ True

# In[3]:


def correctSigns():
    in_string=input("Enter a expression to evaluate")
    out_bool=eval(in_string)
    print(f' {in_string}-->{out_bool}')
    
for i in range(3):
    correctSigns()


# Question3. Create a function that replaces all the vowels in a string with a specified character.
# Examples
# replace_vowels(&quot;the aardvark&quot;, &quot;#&quot;) ➞ &quot;th# ##rdv#rk&quot;
# replace_vowels(&quot;minnie mouse&quot;, &quot;?&quot;) ➞ &quot;m?nn?? m??s?&quot;
# replace_vowels(&quot;shakespeare&quot;, &quot;*&quot;) ➞ &quot;sh*k*sp**r*&quot;

# In[8]:


def replace_vowels():
    vowels=['a','e','i','o','u','A','E','I','O','U']
    in_string=input("Enter a string ")
    in_string_copy=in_string
    out_chr=input("Enter replacement character")
    for ele in in_string:
        if ele in vowels:
            in_string=in_string.replace(ele,out_chr)
    print(f"{in_string_copy}-->{in_string}")
for i in range(3):
          replace_vowels()
    


# Question4. Write a function that calculates the factorial of a number recursively.
# Examples
# factorial(5) ➞ 120
# factorial(3) ➞ 6
# factorial(1) ➞ 1
# factorial(0) ➞ 1

# In[10]:


def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)

print(f'factorial(5) ➞ {factorial(5)}')
print(f'factorial(3) ➞ {factorial(3)}')
print(f'factorial(1) ➞ {factorial(1)}')
print(f'factorial(0) ➞ {factorial(0)}')


# Question 5
# Hamming distance is the number of characters that differ between two strings.
# To illustrate:
# String1: &quot;abcbba&quot;
# String2: &quot;abcbda&quot;
# Hamming Distance: 1 - &quot;b&quot; vs. &quot;d&quot; is the only difference.
# Create a function that computes the hamming distance between two strings.
# Examples
# hamming_distance(&quot;abcde&quot;, &quot;bcdef&quot;) ➞ 5
# hamming_distance(&quot;abcde&quot;, &quot;abcde&quot;) ➞ 0
# hamming_distance(&quot;strong&quot;, &quot;strung&quot;) ➞ 1

# In[11]:


def haming_Distance():
    in_string1=input("Enter first string")
    in_string2=input("Enter second string")
    if len(in_string1)==len(in_string2):
        count=0
        for i in range(len(in_string1)):
            if in_string1[i]!=in_string2[i]:
                count=count+1
        print(f" haming distance between two strings are -->{count}")
    else :
        print("Two strings are same")
for i in range(3):
    haming_Distance()


# In[ ]:




