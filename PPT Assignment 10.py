#!/usr/bin/env python
# coding: utf-8

# # Question 1
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.
# 

# In[1]:


def isPowerOfThree(n):
    if n <= 0:
        return False

    while n % 3 == 0:
        n /= 3

    return n == 1


# In[2]:


isPowerOfThree(27)


# In[3]:


isPowerOfThree(0)


# In[4]:


isPowerOfThree(-1)


# # Question 2
# You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following algorithm on arr:
# •	Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
# •	Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
# •	Keep repeating the steps again, alternating left to right and right to left, until a single number remains.
# Given the integer n, return the last number that remains in arr.
# Input: n = 9
# Output: 6

# In[5]:


def lastRemaining(n):
    return remainingHelper(n, True)

def remainingHelper(n, isLeftToRight):
    if n == 1:
        return 1

    if isLeftToRight or n % 2 == 1:
        
        return 2 * remainingHelper(n // 2, not isLeftToRight)
    else:
        
        return 2 * remainingHelper(n // 2, not isLeftToRight) - 1


# In[6]:


lastRemaining(9)


# In[7]:


lastRemaining(1)


# # Question 3
# ****Given a set represented as a string, write a recursive code to print all subsets of it. The subsets can be printed in any order.
# Example 1:
# Input :  set = “abc”
# Output : { “”, “a”, “b”, “c”, “ab”, “ac”, “bc”, “abc”}
# Example 2:
# Input : set = “abcd”
# Output : { “”, “a” ,”ab” ,”abc” ,”abcd”, “abd” ,”ac” ,”acd”, “ad” ,”b”, “bc” ,”bcd” ,”bd” ,”c” ,”cd” ,”d” }
# 

# In[8]:


def printSubsets(s):
    subsetsHelper(s, "", 0)

def subsetsHelper(s, currentSubset, index):
    if index == len(s):
       
        print(currentSubset)
        return

   
    subsetsHelper(s, currentSubset + s[index], index + 1)

   
    subsetsHelper(s, currentSubset, index + 1)


# In[9]:


printSubsets("abc")


# In[10]:


printSubsets("abcd")


# # Question 4
# Given a string calculate length of the string using recursion.
# 

# In[11]:


def calculateLength(s):
    if s == "":
        return 0
    else:
        return 1 + calculateLength(s[1:])


# In[12]:


calculateLength("abcd")


# In[13]:


calculateLength("GEEKSFORGEEKS")


# # Question 5
# We are given a string S, we need to find count of all contiguous substrings starting and ending with same character.
# 

# In[14]:


def countSubstringsWithSameStartAndEnd(S):
    count = 0

   
    for i in range(len(S)):
       
        for j in range(i, len(S)):
           
            if S[i] == S[j]:
                count += 1

    return count


# In[15]:


countSubstringsWithSameStartAndEnd("abcab")


# In[16]:


countSubstringsWithSameStartAndEnd("aba")


# # Question 6
# The tower of Hanoi is a famous puzzle where we have three rods and N disks. The objective of the puzzle is to move the entire stack to another rod. You are given the number of discs N. Initially, these discs are in the rod 1. You need to print all the steps of discs movement so that all the discs reach the 3rd rod. Also, you need to find the total moves.Note: The discs are arranged such that the top disc is numbered 1 and the bottom-most disc is numbered N. Also, all the discs have different sizes and a bigger disc cannot be put on the top of a smaller disc. Refer the provided link to get a better clarity about the puzzle.
# 

# In[43]:


def towerOfHanoi(n, source=0, destination=0, auxiliary=0):
    if n == 1:
        print("Move disk 1 from rod", source, "to rod", destination)
        return 1
    else:
        moves = 0

      
        moves += towerOfHanoi(n - 1, source, auxiliary, destination)

       
        print("Move disk", n, "from rod", source, "to rod", destination)
        moves += 1

        
        moves += towerOfHanoi(n - 1, auxiliary, destination, source)

        return moves


# In[44]:


towerOfHanoi(2,1,2,3)


# In[25]:


towerOfHanoi(3,1,2)


# # Question 7
# Given a string str, the task is to print all the permutations of str. A permutation is an arrangement of all or part of a set of objects, with regard to the order of the arrangement. For instance, the words ‘bat’ and ‘tab’ represents two distinct permutation (or arrangements) of a similar three letter word.
# 

# In[34]:


def permute(s):
    
    chars = list(s)
    result = []

    
    def permuteHelper(start):
        if start == len(chars) - 1:
           
            result.append("".join(chars))
        else:
           
            for i in range(start, len(chars)):
               
                chars[start], chars[i] = chars[i], chars[start]

               
                permuteHelper(start + 1)

                
                chars[start], chars[i] = chars[i], chars[start]

    
    permuteHelper(0)

    return result




      


# In[35]:


permute("cd")


# In[36]:


permute("abb")


# # Question 8
# Given a string, count total number of consonants in it. A consonant is an English alphabet character that is not vowel (a, e, i, o and u). Examples of constants are b, c, d, f, and g.
# 

# In[40]:


def countConsonants(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0

    for char in s:
        if char in consonants:
            count += 1

    return count



# In[41]:


countConsonants("abc de")


# In[42]:


countConsonants("geeksforgeeks portal")


# In[ ]:




