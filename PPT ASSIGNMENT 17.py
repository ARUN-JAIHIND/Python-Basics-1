#!/usr/bin/env python
# coding: utf-8

# # Question 1
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# 

# In[1]:


def first_non_repeating_character(s):
    char_count = {}

    # Count occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the first non-repeating character
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i

    return -1

# Example usage:
s = "leetcode"
result = first_non_repeating_character(s)
print(result)  # Output: 0


# In[2]:


first_non_repeating_character("leetcode")


# In[3]:


first_non_repeating_character("loveleetcode")


# In[4]:


first_non_repeating_character("aabb")


# # Question 2
# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
# 
# 

# In[5]:


def max_subarray_sum_circular(nums):
    n = len(nums)

    # Case 1: Maximum subarray sum without circular wrapping
    max_sum = kadane(nums)

    # Case 2: Maximum subarray sum with circular wrapping
    total_sum = sum(nums)
    min_sum = kadane([-num for num in nums])

    # If all elements are negative, the maximum subarray sum is the maximum element
    if min_sum == -total_sum:
        return max_sum

    max_sum_circular = total_sum + min_sum

    return max(max_sum, max_sum_circular)

def kadane(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum



# In[6]:


max_subarray_sum_circular([1,-2,3,-2])


# In[7]:


max_subarray_sum_circular([5,-3,5])


# In[8]:


max_subarray_sum_circular([-3,-2,-3])


# # Question 3
# The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.
# The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:
# •	If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
# •	Otherwise, they will leave it and go to the queue's end.
# This continues until none of the queue students want to take the top sandwich and are thus unable to eat.
# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the ith sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the jth student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.
# 
# 

# In[9]:


def count_students_unable_to_eat(students, sandwiches):
    unable_to_eat = 0
    queue = students

    while queue and sandwiches:
        if queue[0] == sandwiches[0]:
            queue.pop(0)
            sandwiches.pop(0)
        else:
            unable_to_eat += 1
            queue.append(queue.pop(0))

    return unable_to_eat


# In[10]:


count_students_unable_to_eat([1,1,0,0],  [0,1,0,1])


# # Question 4
# You have a RecentCounter class which counts the number of recent requests within a certain time frame.
# Implement the RecentCounter class:
# •	RecentCounter() Initializes the counter with zero recent requests.
# •	int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
# 
# 

# In[11]:


class RecentCounter:
    def __init__(self):
        self.requests = []

    def ping(self, t):
        # Add the new request to the list
        self.requests.append(t)

        # Remove the requests that are outside the time frame [t - 3000, t]
        while self.requests[0] < t - 3000:
            self.requests.pop(0)

        # Return the number of remaining requests in the time frame
        return len(self.requests)


# # Question 5
# There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.
# The rules of the game are as follows:
# 1.	Start at the 1st friend.
# 2.	Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
# 3.	The last friend you counted leaves the circle and loses the game.
# 4.	If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
# 5.	Else, the last friend in the circle wins the game.
# Given the number of friends, n, and an integer k, return the winner of the game.
# 
# 

# In[15]:


def find_winner(n, k):
    friends = list(range(1, n+1))
    current = 0

    while len(friends) > 1:
        current = (current + k - 1) % len(friends)
        friends.pop(current)
        if current == len(friends):
            current = 0

    return friends[0]

# Example usage:
n = 5
k = 2
winner = find_winner(n, k)
print(winner)  # Output: 3


# In[16]:


find_winner(5,2)


# In[17]:


find_winner(6,5)


# # Question 6
# You are given an integer array deck. There is a deck of cards where every card has a unique integer. The integer on the ith card is deck[i].
# You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.
# You will do the following steps repeatedly until all cards are revealed:
# 1.	Take the top card of the deck, reveal it, and take it out of the deck.
# 2.	If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
# 3.	If there are still unrevealed cards, go back to step 1. Otherwise, stop.
# Return an ordering of the deck that would reveal the cards in increasing order.
# 
# 

# In[20]:


from collections import deque

def reveal_cards_increasing_order(deck):
    deck.sort()  # Sort the deck in ascending order
    revealed = deque()

    for card in reversed(deck):
        if revealed:
            revealed.appendleft(revealed.pop())  # Move the last card to the front
        revealed.appendleft(card)  # Add the current card to the front

    return list(revealed)



# In[21]:


reveal_cards_increasing_order([17,13,11,2,3,5,7])


# In[22]:


reveal_cards_increasing_order([1,1000])


# # Question 7
# Design a queue that supports push and pop operations in the front, middle, and back.
# Implement the FrontMiddleBack class:
# •	FrontMiddleBack() Initializes the queue.
# •	void pushFront(int val) Adds val to the front of the queue.
# •	void pushMiddle(int val) Adds val to the middle of the queue.
# •	void pushBack(int val) Adds val to the back of the queue.
# •	int popFront() Removes the front element of the queue and returns it. If the queue is empty, return 1.
# •	int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return 1.
# •	int popBack() Removes the back element of the queue and returns it. If the queue is empty, return 1.
# Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:
# •	Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
# •	Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6]. 
# 
# 

# In[26]:


class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class FrontMiddleBack:
    def __init__(self):
        self.head = None
        self.middle = None
        self.size = 0

    def pushFront(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            self.middle = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            if self.size % 2 == 0:
                self.middle = self.middle.prev
        self.size += 1

    def pushMiddle(self, val):
        if not self.head:
            self.pushFront(val)
            return

        new_node = ListNode(val)
        if self.size % 2 == 0:
            self.middle = self.middle.prev

        new_node.next = self.middle.next
        if self.middle.next:
            self.middle.next.prev = new_node
        self.middle.next = new_node
        new_node.prev = self.middle
        self.middle = new_node
        self.size += 1

    def pushBack(self, val):
        if not self.head:
            self.pushFront(val)
            return

        new_node = ListNode(val)
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

        if self.size % 2 == 0:
            self.middle = self.middle.next
        self.size += 1

    def popFront(self):
        if not self.head:
            return -1

        val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None

        if self.size % 2 != 0:
            self.middle = self.middle.next
        self.size -= 1

        return val

    def popMiddle(self):
        if not self.head:
            return -1

        val = self.middle.val

        if self.middle.prev:
            self.middle.prev.next = self.middle.next
        if self.middle.next:
            self.middle.next.prev = self.middle.prev

        if self.size % 2 == 0:
            self.middle = self.middle.next
        else:
            self.middle = self.middle.prev

        self.size -= 1

        return val

    def popBack(self):
        if not self.head:
            return -1

        current = self.head
        while current.next:
            current = current.next

        val = current.val
        if current.prev:
            current.prev.next = None
        else:
            self.head = None

        if self.size % 2 == 0:
            self.middle = self.middle.prev

        self.size -= 1

        return val


# # Question 8
# For a stream of integers, implement a data structure that checks if the last k integers parsed in the stream are equal to value.
# Implement the DataStream class:
# •	DataStream(int value, int k) Initializes the object with an empty integer stream and the two integers value and k.
# •	boolean consec(int num) Adds num to the stream of integers. Returns true if the last k integers are equal to value, and false otherwise. If there are less than k integers, the condition does not hold true, so returns false. 
# 
# 

# In[36]:


from collections import deque

class DataStream:
    def __init__(self, value, k):
        self.stream = deque()
        self.value = value
        self.k = k

    def consec(self, num):
        self.stream.append(num)

        if len(self.stream) >= self.k:
            if len(set(self.stream[-self.k:])) == 1 and self.stream[-1] == self.value:
                return True

        return False
   


