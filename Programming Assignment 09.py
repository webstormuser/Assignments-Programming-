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


# # 1. Write a Python program to check if the given number is a Disarium Number?

# A number is said to be the Disarium number when the sum of its digit raised to the power of their respective positions becomes equal to the number itself.
# Example 175
# power(1)+2 power(7)+ 3 power(5)= 175
# 1+49+125=175 hence 175 is Disarium number

# In[3]:


def calculateLength(n):
    length=0
    while(n!=0):
        length=length+1
        n=n//10
    return length
def checkDisarium():
    num=int(input("Enter num"))
    logging.info(f'Entereed number is {num}')
    length=calculateLength(num)
    sum1=0
    temp=num
    while (num!=0):
        rem=num%10
        sum1=sum1+pow(rem,length)
        num=num//10
        length=length-1
    if sum1==temp:
        logging.info("Number is disarium ")
    else:
        logging.info("Number is not a disarium")
        
checkDisarium()


# # 2. Write a Python program to print all disarium numbers between 1 to 100?

# In[4]:


def calculateLength(n):
    length=0
    while(n!=0):
        length=length+1
        n=n//10
    return length
def checkDisarium(num):
        length=calculateLength(num)
        sum1=0
        temp=num
        while (num!=0):
            rem=num%10
            sum1=sum1+pow(rem,length)
            num=num//10
            length=length-1
        return sum1
init_result=0
disaruim_range=[]
for i in range(1,101):
    init_result=checkDisarium(i)
    if init_result==i:
        disaruim_range.append(i)
logging.info(f' Disarium numbers in range 1 to 100 are : {disaruim_range}')


# # 3. Write a Python program to check if the given number is Happy Number?

# Happy number in python is represented by following process:
#     Starting with any positive integer ,replace number by sum of sqaure of its digits repeat the process untill number =1 or it loops endlessly in a cycle which does not include 1.Those numbers for which this process ends in 1 are happy numbers else not happy numbers 

# Example 49
#    sqaure(4)+sqaure(9)=16+81=97
#    
#    sqaure(9)+sqaure(7)=81+49=130
#    
#    sqaure(1)+sqaure(3)+sqaure(0)=1+9+0=10
#    
#    sqaure(1)+sqaure(0)=1
#    
# it ends with 1 hence it is "Happy number"

# In[5]:


def checkHappyNumber(num):
    try:
        x=num
        while x>=10:
            sum1=0
            while x>0:
                rem=x%10
                sum1=sum1+(rem**2)
                x=x//10
                #print(sum1)
            x=sum1
        if x==1:
            logging.info(f' {num} is a happy number')
        else:
            logging.info(f' {num} is not a happy number')
        if type(num)!=int:
            raise Exception("Enter valid numeric data only")
    except Exception as e:
        logging.exception(e)
num=int(input("Enter number"))
checkHappyNumber(num)


# # 4. Write a Python program to print all happy numbers between 1 and 100?

# In[11]:


def checkHappyNumber(num):
    try:
        rem=sum1=0
        while num>0:
                rem=num%10
                sum1=sum1+(rem**2)
                num=num//10
        return sum1
    except Exception as e:
        logging.exception(e)
HappyNumbers=[]
logging.info("All happy numbers in range 1-100")
for i in range(1,101):
    result=i
    while (result!=1 and result!=4):
        result=checkHappyNumber(result)
    if result==1:
        HappyNumbers.append(i)
logging.info(HappyNumbers)      


# # 5. Write a Python program to determine whether the given number is a Harshad Number?

# Harshad number in python is a number if number is divisible by sum of its digit.
# 
# 
# Example  156 
# 156 s divisible by (1+5+6=12)==>156/12=0

# In[7]:


def checkHarshadNumber(num):
    temp=num
    sum1=0
    while temp!=0:
        rem=temp%10
        sum1=sum1+rem
        temp=temp//10
    if num%sum1==0:
        logging.info("Number is harshad")
    else :
        logging.info("Number is not harshad")
num=int(input("Enter number"))
logging.info(f'Entered number is {num}')
checkHarshadNumber(num)


# # 6. Write a Python program to print all pronic numbers between 1 and 100?

# In[8]:


#isPronicNumber() will determine whether a given number is a pronic number or not    
def isPronicNumber(num):    
    flag = False;    
        
    for j in range(1, num+1):    
        #Checks for pronic number by multiplying consecutive numbers    
        if((j*(j+1)) == num):    
            flag = True;    
            break;    
    return flag;    
     
#Displays pronic numbers between 1 and 100    
print("Pronic numbers between 1 and 100: ");    
for i in range(1, 101):    
    if(isPronicNumber(i)):    
        logging.info(i)     


# In[ ]:




