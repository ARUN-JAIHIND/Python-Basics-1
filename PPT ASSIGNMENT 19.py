#!/usr/bin/env python
# coding: utf-8

# # 1. Merge k Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# 

# In[1]:


def find132pattern(nums):
    stack = []
    second = float('-inf')
    n = len(nums)
    
    for i in range(n-1, -1, -1):
        if nums[i] < second:
            return True
        
        while stack and stack[-1] < nums[i]:
            second = stack.pop()
        
        stack.append(nums[i])
    
    return False


# # 2. Count of Smaller Numbers After Self
# Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].
# 
# 

# In[2]:


def countSmaller(nums):
    def merge_sort(nums, start, end, aux, counts):
        if start == end:
            return [start]
        
        mid = (start + end) // 2
        left_counts = merge_sort(nums, start, mid, aux, counts)
        right_counts = merge_sort(nums, mid + 1, end, aux, counts)
        
        merged_counts = []
        count = 0
        left_ptr = 0
        right_ptr = 0
        
        while left_ptr < len(left_counts) and right_ptr < len(right_counts):
            left_index = left_counts[left_ptr]
            right_index = right_counts[right_ptr]
            
            if nums[left_index] <= nums[right_index]:
                counts[left_index] += count
                merged_counts.append(left_index)
                left_ptr += 1
            else:
                count += 1
                merged_counts.append(right_index)
                right_ptr += 1
        
        while left_ptr < len(left_counts):
            left_index = left_counts[left_ptr]
            counts[left_index] += count
            merged_counts.append(left_index)
            left_ptr += 1
        
        while right_ptr < len(right_counts):
            right_index = right_counts[right_ptr]
            merged_counts.append(right_index)
            right_ptr += 1
        
        return merged_counts
    
    n = len(nums)
    counts = [0] * n
    aux = [0] * n
    merge_sort(nums, 0, n - 1, aux, counts)
    


# In[3]:


countSmaller([5,2,6,1])


# In[4]:


countSmaller([-1])


# In[5]:


countSmaller([-1,-1])


# # 3. Sort an Array
# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
# 
# 

# In[6]:


def quickSort(nums):
    def partition(nums, start, end):
        pivot = nums[end]
        i = start
        
        for j in range(start, end):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
        nums[i], nums[end] = nums[end], nums[i]
        return i
    
    def sort(nums, start, end):
        if start < end:
            pivot_index = partition(nums, start, end)
            sort(nums, start, pivot_index - 1)
            sort(nums, pivot_index + 1, end)
    
    n = len(nums)
    sort(nums, 0, n - 1)
    return nums


# In[7]:


quickSort([5,2,3,1])


# In[8]:


quickSort([5,1,1,2,0,0])


# # 4. Move all zeroes to end of array
# Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).
# 

# In[9]:


def moveZeroes(nums):
    n = len(nums)
    j = 0
    
    for i in range(n):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    
    while j < n:
        nums[j] = 0
        j += 1
    
    return nums


# In[11]:


moveZeroes([1, 2, 0, 4, 3, 0, 5, 0])


# In[12]:


moveZeroes([1, 2, 0, 0, 0, 3, 6])


# # 5. Rearrange array in alternating positive & negative items with O(1) extra space
# Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is followed by a negative and vice-versa maintaining the order of appearance. The number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear at the end of the array.
# 

# In[20]:


def rearrangeArray(nums):
    n = len(nums)
    i = 0
    j = 0

    while i < n and j < n:
        if nums[i] >= 0 and nums[j] < 0:
            i += 1
            j += 1
        elif nums[i] < 0 and nums[j] >= 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[i] >= 0 and nums[j] >= 0:
            j += 1
        else:
            i += 1
    
    return nums


# In[21]:


rearrangeArray([1, 2, 3, -4, -1, 4])


# In[22]:


rearrangeArray([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8])


# # 6. Merge two sorted arrays
# Given two sorted arrays, the task is to merge them in a sorted manner
# 

# In[24]:


def mergeSortedArrays(nums1, nums2):
    merged = []
    i = 0
    j = 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1
    
    while j < len(nums2):
        merged.append(nums2[j])
        j += 1
    
    return merged


# In[25]:


mergeSortedArrays([1, 3, 4, 5],[2, 4, 6, 8])


# In[26]:


mergeSortedArrays([ 5, 8, 9],[4, 7, 8])


# # 7. Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
# 
# 
# 

# In[27]:


def intersection(nums1, nums2):
    set_nums1 = set(nums1)
    intersection = []
    
    for num in nums2:
        if num in set_nums1:
            intersection.append(num)
            set_nums1.remove(num)
    
    return intersection


# In[28]:


intersection([1,2,2,1],[2,2])


# In[29]:


intersection([4,9,5],[9,4,9,8,4])


# # 8. Intersection of Two Arrays II
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
# 
# 

# In[30]:


from collections import Counter

def intersect(nums1, nums2):
    count_nums1 = Counter(nums1)
    intersection = []
    
    for num in nums2:
        if count_nums1.get(num, 0) > 0:
            intersection.append(num)
            count_nums1[num] -= 1
    
    return intersection


# In[31]:


intersect([1,2,2,1],[2,2])


# In[32]:


intersect([4,9,5],[9,4,9,8,4])

