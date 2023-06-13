#!/usr/bin/env python
# coding: utf-8

# # Question 1
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# •	For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python. 
# 

# In[1]:


def mySqrt(x):
    if x == 0:
        return 0
    
    left, right = 1, x
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == x:
            return mid
        
        if square < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right



# In[2]:


mySqrt(4)


# In[3]:


mySqrt(8)


# # Question 2
# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
# You must write an algorithm that runs in O(log n) time.
# 

# In[4]:


def findPeakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left



# In[5]:


findPeakElement([1,2,3,1])


# In[6]:


findPeakElement([1,2,1,3,5,6,4])


# # Question 3
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# 

# In[7]:


def missingNumber(nums):
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    missing_number = expected_sum - actual_sum
    return missing_number



# In[8]:


missingNumber([3,0,1])


# In[9]:


missingNumber([0,1])


# In[10]:


missingNumber([9,6,4,2,3,5,7,0,1])


# # Question 4
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.
# 

# In[11]:


def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    
    ptr = nums[0]
    while ptr != slow:
        ptr = nums[ptr]
        slow = nums[slow]

    return ptr



# In[12]:


findDuplicate([1,3,4,2,2])


# In[13]:


findDuplicate([3,1,3,4,2])


# # Question 5
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
# 

# In[15]:


def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    intersection_set = set()

    for num in set1:
        if num in set2:
            intersection_set.add(num)

    return list(intersection_set)



# In[16]:


intersection([1,2,2,1],[2,2])


# In[17]:


intersection([4,9,5], [9,4,9,8,4])


# # Question 6
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
# •	[4,5,6,7,0,1,2] if it was rotated 4 times.
# •	[0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.
# 

# In[18]:


def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]



# In[19]:


findMin([3,4,5,1,2])


# In[20]:


findMin([4,5,6,7,0,1,2])


# In[21]:


findMin([11,13,15,17])


# # Question 7
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
# 

# In[22]:


def searchRange(nums, target):
    start = -1
    end = -1

    
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            start = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    
    left = start
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            end = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return [start, end]



# In[23]:


searchRange([5,7,7,8,8,10],8)


# In[24]:


searchRange([5,7,7,8,8,10],6)


# In[26]:


searchRange([1],0)


# # Question 8
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
# 

# In[28]:


def intersect(nums1, nums2):
    frequency_map = {}
    for num in nums1:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1

    intersection = []
    for num in nums2:
        if num in frequency_map and frequency_map[num] > 0:
            intersection.append(num)
            frequency_map[num] -= 1

    return intersection



# In[29]:


intersect([1,2,2,1],[2,2])


# In[30]:


intersect([4,9,5],[9,4,9,8,4])


# In[ ]:




