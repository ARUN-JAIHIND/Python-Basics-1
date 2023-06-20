#!/usr/bin/env python
# coding: utf-8

# # Question 1
# Given an array arr[ ] of size N having elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.Next greater element of an element in the array is the nearest element on the right which is greater than the current element.If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.
# 

# In[1]:


def find_next_greater(arr):
    stack = []
    result = []

    # Iterate the array from right to left
    for i in range(len(arr)-1, -1, -1):
        # Pop elements from stack while they are smaller than or equal to current element
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        # If stack is empty, there is no greater element on the right
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        # Push the current element onto the stack
        stack.append(arr[i])

    # Reverse the result array
    result.reverse()
    return result


# # Question 2
# Given an array a of integers of length n, find the nearest smaller number for every element such that the smaller element is on left side.If no small element present on the left print -1.
# 

# In[2]:


def find_nearest_smaller(a):
    stack = []
    result = []

    # Iterate the array from left to right
    for i in range(len(a)):
        # Pop elements from stack while they are greater than or equal to current element
        while stack and stack[-1] >= a[i]:
            stack.pop()

        # If stack is empty, there is no smaller element on the left
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        # Push the current element onto the stack
        stack.append(a[i])

    return result


# # Question 3
# Implement a Stack using two queues q1 and q2.
# 

# In[3]:


class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, element):
        self.q1.append(element)

    def pop(self):
        if not self.q1:
            return None

        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        popped_element = self.q1.pop(0)

        self.q1, self.q2 = self.q2, self.q1

        return popped_element

    def top(self):
        if not self.q1:
            return None

        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        top_element = self.q1[0]

        self.q2.append(self.q1.pop(0))

        self.q1, self.q2 = self.q2, self.q1

        return top_element

    def empty(self):
        return not self.q1 and not self.q2


# # Question 4
# You are given a stack St. You have to reverse the stack using recursion.
# 

# In[4]:


def reverse_stack(stack):
    if len(stack) <= 1:
        return stack

    top_element = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top_element)

def insert_at_bottom(stack, element):
    if len(stack) == 0:
        stack.append(element)
    else:
        top = stack.pop()
        insert_at_bottom(stack, element)
        stack.append(top)
stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)  


# In[6]:


insert_at_bottom([3,2,1,7,6],2)


# # Question 5
# You are given a string S, the task is to reverse the string using stack.
# 

# In[9]:


def reverse_string(string):
    stack = []
    reversed_string = ""

    # Push each character onto the stack
    for char in string:
        stack.append(char)

    # Pop each character from the stack and append it to the reversed string
    while stack:
        reversed_string += stack.pop()

    return reversed_string
S = GeeksforGeeks"
reversed_S = reverse_string(S)
print(reversed_S)  


# # Question 6
# Given string S representing a postfix expression, the task is to evaluate the expression and find the final value. Operators will only include the basic arithmetic operators like *, /, + and -.
# 
# 
# 

# In[15]:


def evaluate_postfix(expression):
    stack = []

    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2

            stack.append(result)

    return stack.pop()
S = "231*+9-"
result = evaluate_postfix(S)
print(result)


# # Question 7
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# •	MinStack() initializes the stack object.
# •	void push(int val) pushes the element val onto the stack.
# •	void pop() removes the element on the top of the stack.
# •	int top() gets the top element of the stack.
# •	int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.
# 
# 

# In[16]:


class MinStack:
    def __init__(self):
        self.stack = []  # Stack to store elements
        self.min_stack = []  # Stack to store minimum elements

    def push(self, val):
        self.stack.append(val)  # Push the element to the main stack

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)  # Push the element to the min stack if it is empty or smaller than the current minimum

    def pop(self):
        if self.stack:
            element = self.stack.pop()

            if element == self.min_stack[-1]:
                self.min_stack.pop()  # Pop the element from the min stack if it is equal to the current minimum

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
stack = MinStack()
stack.push(5)
stack.push(2)
stack.push(7)
stack.push(1)

print(stack.top())  # Output: 1
print(stack.getMin())  # Output: 1

stack.pop()

print(stack.top())  # Output: 7
print(stack.getMin())  # Output: 2


# # Question 8
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# 
# 

# In[17]:


def trap_water(heights):
    left = 0
    right = len(heights) - 1
    left_max = right_max = total_water = 0

    while left <= right:
        if heights[left] <= heights[right]:
            left_max = max(left_max, heights[left])
            total_water += left_max - heights[left]
            left += 1
        else:
            right_max = max(right_max, heights[right])
            total_water += right_max - heights[right]
            right -= 1

    return total_water
elevation_map = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
water_trapped = trap_water(elevation_map)
print(water_trapped)  


# In[ ]:




