#!/usr/bin/env python
# coding: utf-8

# # 1. Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
# 

# In[1]:


def merge_intervals(intervals):
    # Sort the intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    # Initialize the result array
    merged = []

    for interval in intervals:
        # If the result array is empty or the current interval does not overlap
        # with the previous merged interval, add the current interval to the result array
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            # Merge the current interval with the previous merged interval
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


# In[2]:


merge_intervals([[1,3],[2,6],[8,10],[15,18]])


# In[3]:


merge_intervals([[1,4],[4,5]])


# # 2. Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
# 
# 

# In[4]:


def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


# In[5]:


sort_colors([2,0,2,1,1,0])


# In[6]:


sort_colors([2,0,1])


# # 3. First Bad Version Solution
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
# 
# 

# In[14]:


def first_bad_version(n):
    left = 1
    right = n

    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left


# # 4. Maximum Gap
# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.
# You must write an algorithm that runs in linear time and uses linear extra space.
# 
# 

# In[11]:


def maximum_gap(nums):
    if len(nums) < 2:
        return 0

    # Find the maximum element in the array
    max_num = max(nums)

    # Perform Radix Sort
    exp = 1
    n = len(nums)
    sorted_nums = [0] * n

    while max_num // exp > 0:
        count = [0] * 10

        # Counting sort based on the current digit (exp)
        for i in range(n):
            count[(nums[i] // exp) % 10] += 1

        # Calculate cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the sorted array
        for i in range(n - 1, -1, -1):
            index = (nums[i] // exp) % 10
            sorted_nums[count[index] - 1] = nums[i]
            count[index] -= 1

        # Update the original array with the sorted array
        nums = sorted_nums.copy()

        exp *= 10

    # Calculate the maximum gap
    max_gap = 0
    for i in range(1, n):
        max_gap = max(max_gap, nums[i] - nums[i - 1])

    return max_gap


# In[12]:


maximum_gap( [3,6,9,1])


# In[13]:


maximum_gap([10])


# # 5. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# 

# In[1]:


def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# In[2]:


containsDuplicate([1,2,3,1])


# In[3]:


containsDuplicate([1,2,3,4])


# In[4]:


containsDuplicate([1,1,1,3,3,4,3,2,4,2])


# # 6. Minimum Number of Arrows to Burst Balloons
# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
# 
# 

# In[5]:


def findMinArrowShots(points):
    if not points:
        return 0
    
    points.sort(key=lambda x: x[1])  # Sort balloons based on ending points
    end = points[0][1]  # Track the end position of the first balloon
    arrows = 1  # At least one arrow is needed
    
    for i in range(1, len(points)):
        if points[i][0] > end:
            # Current balloon's start position is greater than 'end'
            # Shoot an arrow to burst previous balloons and update 'end'
            arrows += 1
            end = points[i][1]
    
    return arrows


# In[6]:


findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])


# In[7]:


findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])


# In[8]:


findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])


# # 7. Longest Increasing Subsequence
# Given an integer array nums, return the length of the longest strictly increasing
# 

# In[9]:


def lengthOfLIS(nums):
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


# In[10]:


lengthOfLIS( [10,9,2,5,3,7,101,18])


# In[11]:


lengthOfLIS([0,1,0,3,2,3])


# In[12]:


lengthOfLIS([7,7,7,7,7,7,7])


# # 8. 132 Pattern
# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
# Return true if there is a 132 pattern in nums, otherwise, return false.
# 

# In[13]:


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


# In[14]:


find132pattern([1,2,3,4])


# In[15]:


find132pattern([3,1,4,2])


# In[16]:


find132pattern([-1,3,2,0])

