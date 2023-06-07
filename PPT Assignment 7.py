#!/usr/bin/env python
# coding: utf-8

# # Question 1
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# In[1]:


def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    s_map = {}
    t_map = {}
    mapped_s = ""
    
    for s_char, t_char in zip(s, t):
        if s_char in s_map:
            mapped_s += s_map[s_char]
        else:
            if t_char in t_map:
                return False
            s_map[s_char] = t_char
            t_map[t_char] = s_char
            mapped_s += t_char
    
    return mapped_s == t


# In[2]:


is_isomorphic(s = "egg", t = "add")


# # Question 2
# Given a string num which represents an integer, return true if num is a strobogrammatic number.
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Example 1:
# Input: num = "69"
# Output:
# true

# In[3]:


def is_strobogrammatic(num):
    mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    left, right = 0, len(num) - 1
    
    while left <= right:
        if num[left] not in mapping or mapping[num[left]] != num[right]:
            return False
        left += 1
        right -= 1
    
    return True


# In[5]:


is_strobogrammatic("69")


# # Question 3
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
# Example 1:
# Input: num1 = "11", num2 = "123"
# Output:
# "134"

# In[6]:


def addStrings(num1, num2):
    result = ""
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    
    while i >= 0 or j >= 0 or carry:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0
        sum_digits = digit1 + digit2 + carry
        current_digit = sum_digits % 10
        carry = sum_digits // 10
        result = str(current_digit) + result
        i -= 1
        j -= 1
    
    return result


# In[7]:


addStrings("11","123")


# # Question 4
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# In[9]:


def reverseWords(s):
    words = s.split()
    reversed_words = []
    
    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)
    
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence


# In[10]:


reverseWords("Let's take LeetCode contest")


# # Question 5
# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.
# Example 1:
# Input: s = "abcdefg", k = 2
# Output:
# "bacdfeg"

# In[11]:


def reverseStr(s, k):
    s_list = list(s)
    n = len(s)
    
    for i in range(0, n, 2*k):
        s_list[i:i+k] = reversed(s_list[i:i+k])
    
    return ''.join(s_list)


# In[12]:


reverseStr("abcdefg",2)


# # Question 6
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# •	For example, if s = "abcde", then it will be "bcdea" after one shift.
# Example 1:
# Input: s = "abcde", goal = "cdeab"
# Output:
# true

# In[13]:


def rotateString(s, goal):
    concatenated_s = s + s
    return goal in concatenated_s


# In[14]:


rotateString("abcde","cdeab")


# # Question 7
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.
# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation:
# Both s and t become "ac"

# In[15]:


def processString(s):
    processed = []
    
    for char in s:
        if char != '#':
            processed.append(char)
        elif processed:
            processed.pop()
    
    return processed

def buildFinalString(processed):
    return ''.join(processed)

def backspaceCompare(s, t):
    processed_s = processString(s)
    processed_t = processString(t)
    
    return buildFinalString(processed_s) == buildFinalString(processed_t)


# In[18]:


backspaceCompare(s = "ab#c", t = "ad#c")


# # Question 8
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
# Example
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

# In[19]:


def checkStraightLine(coordinates):
    if len(coordinates) <= 2:
        return True

    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    initial_slope = (y2 - y1) / (x2 - x1)

    for i in range(2, len(coordinates)):
        x3, y3 = coordinates[i]
        slope = (y3 - y2) / (x3 - x2)
        if slope != initial_slope:
            return False
        x2, y2 = x3, y3

    return True


# In[20]:


checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])


# In[ ]:




