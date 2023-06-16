#!/usr/bin/env python
# coding: utf-8

# # Question 1
#  Given a linked list of N nodes such that it may contain a loop. A loop here means that the last node of the link list is connected to the node at position X(1-based index). If the link list does not have any loop, X=0. Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.
# 

# In[1]:


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def remove_loop(head):
    # Step 1: Find the meeting point of the slow and fast pointers
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    
    # No loop exists in the list
    if not fast or not fast.next:
        return head
    
    # Step 2: Reset the slow pointer to the head
    slow = head
    
    # Step 3: Move both pointers one step at a time until they meet again
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next
    
    # Step 4: Remove the loop by setting the next pointer of the last node to None
    fast.next = None
    
    return head


# # Question 2
# A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.
# 
# 
# 

# In[6]:


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def addOne(head):
    # Step 1: Reverse the linked list
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    head = prev

    # Step 2: Add 1 to the reversed linked list
    carry = 1
    curr = head
    while curr:
        curr.val += carry
        carry = curr.val // 10
        curr.val %= 10
        if carry == 0:
            break
        curr = curr.next

    # Step 3: Reverse the linked list again
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    head = prev

    # Step 4: If carry is still remaining, create a new head node with value 1
    if carry > 0:
        new_head = ListNode(1)
        new_head.next = head
        head = new_head

    return head


# # Question 3
# Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:(i) a next pointer to the next node,(ii) a bottom pointer to a linked list where this node is head.Each of the sub-linked-list is in sorted order.Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. Note: The flattened list will be printed using the bottom pointer instead of next pointer.
# 

# In[7]:


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.bottom = None

def merge(list1, list2):
    # Merge two sorted linked lists
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val <= list2.val:
        result = list1
        result.bottom = merge(list1.bottom, list2)
    else:
        result = list2
        result.bottom = merge(list1, list2.bottom)

    return result

def flatten(head):
    # Base case: an empty list or a single node
    if not head or not head.next:
        return head

    # Recursively flatten the next node
    head.next = flatten(head.next)

    # Merge the flattened next node with the current node's bottom list
    head = merge(head, head.next)

    return head


# # Question 4
# You are given a special linked list with N nodes where each node has a next pointer pointing to its next node. You are also given M random pointers, where you will be given M number of pairs denoting two nodes a and b  i.e. a->arb = b (arb is pointer to random node).
# Construct a copy of the given list. The copy should consist of exactly N new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
# For example, if there are two nodes X and Y in the original list, where X.arb --> Y, then for the corresponding two nodes x and y in the copied list, x.arb --> y.
# Return the head of the copied linked list.
# 
# 

# In[8]:


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None

def copyRandomList(head):
    if not head:
        return None

    # Step 1: Create a copy of each node and link them together using the next pointer
    current = head
    while current:
        new_node = Node(current.val)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next

    # Step 2: Assign the random pointers of the copied nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Separate the original list and the copied list
    current = head
    new_head = head.next
    new_current = new_head

    while current:
        current.next = current.next.next
        if new_current.next:
            new_current.next = new_current.next.next
        current = current.next
        new_current = new_current.next

    return new_head


# # Question 5
# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.
# 

# In[9]:


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def oddEvenList(head):
    if not head or not head.next:
        return head

    odd_head = odd = head
    even_head = even = head.next

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head

    return odd_head


# # Question 6
# Given a singly linked list of size N. The task is to left-shift the linked list by k nodes, where k is a given positive integer smaller than or equal to length of the linked list.
# 

# In[10]:


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def leftShift(head, k):
    if not head or not head.next:
        return head

    # Step 1: Find the kth node from the beginning of the list
    current = head
    for _ in range(k - 1):
        current = current.next
        if not current:
            return head

    # Step 2: Set the new head of the shifted list
    new_head = current.next

    # Step 3: Traverse to the end of the list
    tail = current
    while tail.next:
        tail = tail.next

    # Step 4: Connect the end of the list to the original head
    tail.next = head

    # Update the next pointer of the kth node to None
    current.next = None

    return new_head


# # Question 7
# You are given the head of a linked list with n nodes.
# For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.
# Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.
# 

# In[11]:


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def nextLargerNodes(head):
    stack = []
    result = []

    # Traverse the linked list in reverse order
    current = head
    while current:
        while stack and stack[-1] <= current.val:
            stack.pop()

        if stack:
            result.append(stack[-1])
        else:
            result.append(0)

        stack.append(current.val)
        current = current.next

    # Reverse the result array
    result.reverse()

    return result


# # Question 8
# Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
# After doing so, return the head of the final linked list.  You may return any such answer.
# (Note that in the examples below, all sequences are serializations of ListNode objects.)
# 

# In[12]:


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def removeZeroSumSublists(head):
    dummy = ListNode(0)
    dummy.next = head

    prefix_sum = 0
    prefix_sum_dict = {0: dummy}

    current = head
    while current:
        prefix_sum += current.val
        if prefix_sum in prefix_sum_dict:
            # Remove the sequence of nodes with a sum of 0
            prev = prefix_sum_dict[prefix_sum]
            start = prev.next
            prefix_sum += start.val
            while start != current:
                del prefix_sum_dict[prefix_sum]
                start = start.next
                prefix_sum += start.val
            prev.next = current.next
        else:
            prefix_sum_dict[prefix_sum] = current
        current = current.next

    return dummy.next


# In[ ]:




