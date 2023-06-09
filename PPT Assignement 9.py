#!/usr/bin/env python
# coding: utf-8

# # Question 1
# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.
# Example 1: Input: n = 1
# Output: true
# Example 2: Input: n = 16
# Output: true
# Example 3: Input: n = 3
# Output: false

# In[1]:


def isPowerOfTwo(n):
    if n <= 0:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True


# In[2]:


isPowerOfTwo(1)


# In[3]:


isPowerOfTwo(16)


# In[4]:


isPowerOfTwo(3)


# # Question 2
# Given a number n, find the sum of the first natural numbers.
# Example 1:
# Input: n = 3
# Output: 6
# Example 2:
# Input : 5
# Output : 15

# In[5]:


def sumOfFirstNNumbers(n):
    return (n * (n + 1)) // 2


# In[6]:


sumOfFirstNNumbers(3)


# In[8]:


sumOfFirstNNumbers(5)


# # Question 3
# ****Given a positive integer, N. Find the factorial of N.
# Example 1:
# Input: N = 5
# Output: 120
# Example 2:
# Input: N = 4
# Output: 24

# In[10]:


def factorial(N):
    result = 1
    for i in range(1, N + 1):
        result *= i
    return result


# In[11]:


factorial(5)


# In[12]:


factorial(4)


# # Question 4
# Given a number N and a power P, the task is to find the exponent of this number raised to the given power, i.e. N^P.
# Example 1 :
# Input: N = 5, P = 2
# Output: 25
# Example 2 : Input: N = 2, P = 5
# Output: 32

# In[13]:


def exponentiation(N, P):
    return N ** P


# In[14]:


exponentiation(5,2)


# In[15]:


exponentiation(2,5)


# # Question 5
# Given an array of integers arr, the task is to find maximum element of that array using recursion.
# Example 1:
# Input: arr = {1, 4, 3, -5, -4, 8, 6}; Output: 8
# Example 2:
# Input: arr = {1, 4, 45, 6, 10, -8}; Output: 45

# In[19]:


def findMax(arr):

    if len(arr) == 1:
        return arr[0]

   
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    
    max_left = findMax(left_half)
    max_right = findMax(right_half)

   
    return max(max_left, max_right)


# In[22]:


findMax([1, 4, 3, -5, -4, 8, 6])


# In[23]:


findMax([1, 4, 45, 6, 10, -8])


# # Question 6
# Given first term (a), common difference (d) and a integer N of the Arithmetic Progression series, the task is to find Nth term of the series.
# Example 1:
# Input : a = 2 d = 1 N = 5 Output : 6 The 5th term of the series is : 6
# Example 2:
# Input : a = 5 d = 2 N = 10 Output : 23 The 10th term of the series is : 23

# In[24]:


def findNthTerm(a, d, N):
    return a + (N - 1) * d


# In[25]:


findNthTerm(2,1,5)


# In[26]:


findNthTerm(5,2,10)


# # Question 7
# Given a string S, the task is to write a program to print all permutations of a given string.
# Example 1:
# Input:
# S = “ABC”
# Output:
# “ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”
# Example 2:
# Input:
# S = “XY”
# Output:
# “XY”, “YX”

# In[30]:


def generatePermutations(S):
    # Convert the string to a list for easier manipulation
    chars = list(S)
    result = []

    def backtrack(start):
       
        if start == len(chars):
            result.append(''.join(chars))
            return

        for i in range(start, len(chars)):
          
            chars[start], chars[i] = chars[i], chars[start]
            
           
            backtrack(start + 1)
            
           
            chars[start], chars[i] = chars[i], chars[start]

    
    backtrack(0)
    
    return result


# In[31]:


generatePermutations("ABC")


# In[32]:


generatePermutations("xy")


# # Question 8
# Given an array, find a product of all array elements.
# Example 1:
# Input : arr[] = {1, 2, 3, 4, 5} Output : 120 Example 2:
# Input : arr[] = {1, 6, 3} Output : 18
# 

# In[33]:


def productOfArrayElements(arr):
    product = 1
    for element in arr:
        product *= element
    return product


# In[34]:


productOfArrayElements([1, 2, 3, 4, 5])


# In[35]:


productOfArrayElements([1,6,3])


# In[ ]:




