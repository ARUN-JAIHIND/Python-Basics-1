#!/usr/bin/env python
# coding: utf-8

# # Question 1
# Given an array, for each element find the value of the nearest element to the right which is having a frequency greater than that of the current element. If there does not exist an answer for a position, then make the value ‘-1’.
# 

# In[3]:


from collections import defaultdict

def find_nearest_right_elements(arr):
    frequency = defaultdict(int)
    stack = []
    nearest_right = [-1] * len(arr)

    # Step 1: Count frequency of each element
    for num in arr:
        frequency[num] += 1

    # Step 3: Find nearest right elements
    for i in range(len(arr)-1, -1, -1):
        while stack and frequency[arr[i]] >= frequency[arr[stack[-1]]]:
            stack.pop()
        if stack:
            nearest_right[i] = arr[stack[-1]]
        stack.append(i)

    return nearest_right



# In[4]:


find_nearest_right_elements([1, 1, 2, 3, 4, 2, 1])


# In[5]:


find_nearest_right_elements([1, 1, 1, 2, 2, 2, 2, 11, 3, 3])


# # Question 2
# Given a stack of integers, sort it in ascending order using another temporary stack.
# 

# In[12]:


def sort_stack(stack):
    temp_stack = []

    while stack:
        temp = stack.pop()

        while temp_stack and temp_stack[-1] < temp:
            stack.append(temp_stack.pop())

        temp_stack.append(temp)

    while temp_stack:
        stack.append(temp_stack.pop())

    return stack


# In[10]:


sort_stack([34, 3, 31, 98, 92, 23])


# In[11]:


sort_stack([3, 5, 1, 4, 2, 8])


# # Question 3
# Given a stack with push(), pop(), and empty() operations, The task is to delete the middle element of it without using any additional data structure.
# 

# In[16]:


def delete_middle_element(stack):
    if stack_empty(stack):
        return stack

    middle_index = len(stack) // 2

    delete_middle_recursive(stack, middle_index)

    return stack

def delete_middle_recursive(stack, current_index):
    if current_index == 0:
        stack.pop()
        return

    temp = stack.pop()
    delete_middle_recursive(stack, current_index - 1)
    stack.append(temp)

def stack_empty(stack):
    return len(stack) == 0


# In[14]:


delete_middle_element([1, 2, 3, 4, 5])


# In[15]:


delete_middle_element([1,2,3,4,5,6])


# # Question 4
# Given a Queue consisting of first n natural numbers (in random order). The task is to check whether the given Queue elements can be arranged in increasing order in another Queue using a stack. The operation allowed are:
# 1.	Push and pop elements from the stack
# 2.	Pop (Or Dequeue) from the given Queue.
# 3.	Push (Or Enqueue) in the another Queue. 
# 
# 

# In[17]:


from queue import Queue

def arrange_in_increasing_order(queue):
    stack = []
    another_queue = Queue()

    while not queue.empty():
        current_element = queue.queue[0]

        if current_element == queue.queue[0]:
            queue.get()
            another_queue.put(current_element)
        elif not stack or stack[-1] > current_element:
            stack.append(current_element)
            queue.get()
        elif not another_queue.empty() and another_queue.queue[-1] > current_element:
            another_queue.put(stack[-1])
            stack.pop()
        else:
            return False

    while stack:
        another_queue.put(stack[-1])
        stack.pop()

    prev_element = another_queue.get()

    while not another_queue.empty():
        current_element = another_queue.get()
        if prev_element >= current_element:
            return False
        prev_element = current_element

    return True

# Example usage:
queue = Queue()
queue.put(3)
queue.put(1)
queue.put(2)

result = arrange_in_increasing_order(queue)
print(result)  # Output: True


# # Question 5
# Given a number , write a program to reverse this number using stack.
# 

# In[21]:


def reverse_number_using_stack(number):
    # Convert number to string
    number_str = str(number)

    # Create an empty stack
    stack = []

    # Push each digit onto the stack
    for digit in number_str:
        stack.append(digit)

    # Create an empty string
    reversed_str = ""

    # Pop digits from stack and append to reversed string
    while stack:
        reversed_str += stack.pop()

    # Convert reversed string back to integer
    reversed_number = int(reversed_str)

    return reversed_number

# Example usage:
number = 12345
result = reverse_number_using_stack(number)
print(result)  # Output: 54321


# In[22]:


reverse_number_using_stack(365)


# In[23]:


reverse_number_using_stack(6899)


# # Question 6
# Given an integer k and a queue of integers, The task is to reverse the order of the first k elements of the queue, leaving the other elements in the same relative order.
# Only following standard operations are allowed on queue.
# •	enqueue(x) : Add an item x to rear of queue
# •	dequeue() : Remove an item from front of queue
# •	size() : Returns number of elements in queue.
# •	front() : Finds front item. 
# 
# 

# In[24]:


from queue import Queue

def reverse_k_elements(queue, k):
    stack = []

    # Step 2: Dequeue the first k elements and push them onto the stack
    for _ in range(k):
        stack.append(queue.get())

    # Step 3: Create an empty temporary queue
    temp_queue = Queue()

    # Step 4: Enqueue elements from stack to temporary queue
    while stack:
        temp_queue.put(stack.pop())

    # Step 5: Enqueue remaining elements from original queue to temporary queue
    while not queue.empty():
        temp_queue.put(queue.get())

    # Step 6: Assign the contents of temporary queue back to original queue
    while not temp_queue.empty():
        queue.put(temp_queue.get())

    return queue

# Example usage:
queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)

k = 3
result = reverse_k_elements(queue, k)
while not result.empty():
    print(result.get(), end=" ")  # Output: 3 2 1 4 5


# # Question 7
# Given a sequence of n strings, the task is to check if any two similar words come together and then destroy each other then print the number of words left in the sequence after this pairwise destruction.
# 
# 

# In[28]:


def pairwise_destruction(sequence):
    stack = []

    for word in sequence:
        if stack and word == stack[-1]:
            stack.pop()
        else:
            stack.append(word)

    return len(stack)



# In[27]:


pairwise_destruction("ab" "aa" "aa" "bcd" "ab")


# In[32]:


pairwise_destruction('tom' 'jerry' 'jerry' 'tom')


# # Question 8
# Given an array of integers, the task is to find the maximum absolute difference between the nearest left and the right smaller element of every element in the array.
# Note: If there is no smaller element on right side or left side of any element then we take zero as the smaller element. For example for the leftmost element, the nearest smaller element on the left side is considered as 0. Similarly, for rightmost elements, the smaller element on the right side is considered as 0.
# 

# In[36]:


def max_absolute_difference(arr):
    stack = []
    n = len(arr)
    left_smaller = [0] * n
    right_smaller = [0] * n

    for i in range(n):
        while stack and stack[-1] > arr[i]:
            right_smaller[stack.pop()] = arr[i]
        stack.append(i)

    stack.clear()

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            left_smaller[stack.pop()] = arr[i]
        stack.append(i)

    max_diff = 0

    for i in range(n):
        diff = abs(right_smaller[i] - left_smaller[i])
        max_diff = max(max_diff, diff)

    return max_diff



# In[35]:


max_absolute_difference([2, 1, 8])


# In[ ]:




