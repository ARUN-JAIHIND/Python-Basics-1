#!/usr/bin/env python
# coding: utf-8

# # Question 1
# Given a singly linked list, delete middle of the linked list. For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5.If there are even nodes, then there would be two middle nodes, we need to delete the second middle element. For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.If the input linked list is NULL or has 1 node, then it should return NULL
# 

# In[3]:


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def delete_middle_node(head):
    if head is None or head.next is None:
        return None

    slow_ptr = head
    fast_ptr = head
    prev_ptr = None

    while fast_ptr is not None and fast_ptr.next is not None:
        fast_ptr = fast_ptr.next.next
        prev_ptr = slow_ptr
        slow_ptr = slow_ptr.next

    prev_ptr.next = slow_ptr.next
    slow_ptr = None

    return head
# Create the linked list: 1->2->3->4->5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Delete the middle node
head = delete_middle_node(head)



# # Question 2
# Given a linked list of N nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.
# 

# In[10]:


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def has_loop(head):
    if head is None or head.next is None:
        return False

    slow_ptr = head
    fast_ptr = head.next

    while fast_ptr is not None and fast_ptr.next is not None:
        if slow_ptr == fast_ptr:
            return True

        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return False
# Create the linked list: 1->2->3->4->5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Check if the linked list has a loop
has_loop_result = has_loop(head)
print(has_loop_result)  # Output: False

# Create a loop in the linked list: 2->3->4->5->2 (self loop)
head.next.next.next.next.next = head.next

# Check if the linked list has a loop
has_loop_result = has_loop(head)
print(has_loop_result)  # Output: True


# # Question 3
# Given a linked list consisting of L nodes and given a number N. The task is to find the Nth node from the end of the linked list.
# 

# In[14]:


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def find_nth_from_end(head, n):
    if head is None:
        return None

    first_ptr = head
    second_ptr = head

    # Move first_ptr N nodes ahead
    for _ in range(n):
        if first_ptr is None:
            return None  # N is greater than the length of the linked list
        first_ptr = first_ptr.next

    while first_ptr is not None:
        first_ptr = first_ptr.next
        second_ptr = second_ptr.next

    return second_ptr.data
# Create the linked list: 1->2->3->4->5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Find the 2nd node from the end
nth_node = find_nth_from_end(head, 2)
print(nth_node)  # Output: 4

# Find the 6th node from the end
nth_node = find_nth_from_end(head, 6)
print(nth_node)  # Output: None (N is greater than the length of the linked list)


# # Question 4
# Given a singly linked list of characters, write a function that returns true if the given list is a palindrome, else false.
# 
# 

# In[15]:


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def is_palindrome(head):
    if head is None or head.next is None:
        return True

    stack = []
    slow_ptr = head
    fast_ptr = head

    # Traverse the linked list and store characters in the stack
    while fast_ptr is not None and fast_ptr.next is not None:
        stack.append(slow_ptr.data)
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    # Handle odd length of linked list
    if fast_ptr is not None:
        slow_ptr = slow_ptr.next

    # Compare characters with the stack
    while slow_ptr is not None:
        if slow_ptr.data != stack.pop():
            return False
        slow_ptr = slow_ptr.next

    return True
# Create the linked list: r->a->d->a->r
head = Node('r')
head.next = Node('a')
head.next.next = Node('d')
head.next.next.next = Node('a')
head.next.next.next.next = Node('r')

# Check if the linked list is a palindrome
is_palindrome_result = is_palindrome(head)
print(is_palindrome_result)  # Output: True

# Create the linked list: h->e->l->l->o
head = Node('h')
head.next = Node('e')
head.next.next = Node('l')
head.next.next.next = Node('l')
head.next.next.next.next = Node('o')

# Check if the linked list is a palindrome
is_palindrome_result = is_palindrome(head)
print(is_palindrome_result)  # Output: False


# # Question 5
# Given a linked list of N nodes such that it may contain a loop.
# A loop here means that the last node of the link list is connected to the node at position X(1-based index). If the link list does not have any loop, X=0.
# Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.
# 

# In[18]:


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def detect_and_remove_loop(head):
    if head is None or head.next is None:
        return head

    slow_ptr = head
    fast_ptr = head

    # Detect the loop and find the node where the loop starts
    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            break

    # If no loop is detected
    if fast_ptr is None or fast_ptr.next is None:
        return head

    # Move one of the pointers back to the head
    slow_ptr = head

    # Find the node where the loop starts
    while slow_ptr.next != fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next

    # Break the loop by setting the next pointer to None
    fast_ptr.next = None

    return head
# Create the linked list: 1->2->3->4->5->6 (with a loop from 6 to 3)
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = head.next.next.next  # Create a loop

# Remove the loop from the linked list
head = detect_and_remove_loop(head)

# Print the modified linked list
current = head
while current is not None:
    print(current.data, end="->")
    current = current.next


# # Question 6
# 
# Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same till end of the linked list.
# 
# Difficulty Level: Rookie

# In[19]:


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def retain_delete(head, M, N):
    if head is None or M <= 0 or N <= 0:
        return head

    current = head

    while current is not None:
        # Traverse M nodes
        for _ in range(M - 1):
            if current is None:
                return head  # Reached the end of the linked list
            current = current.next

        if current is None:
            return head  # Reached the end of the linked list

        # Delete N nodes
        temp = current.next
        for _ in range(N):
            if temp is None:
                break
            temp = temp.next

        # Set the next pointer of the current node to the next node after deleting N nodes
        current.next = temp
        current = temp

    return head
# Create the linked list: 1->2->3->4->5->6->7->8->9->10
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)
head.next.next.next.next.next.next.next.next.next = Node(10)

# Retain 2 nodes, delete the next 3 nodes, continue till the end of the linked list
modified_head = retain_delete(head, 2, 3)

# Print the modified linked list
current = modified_head
while current is not None:
    print(current.data, end="->")
    current = current.next


# # Question 7
# 
# Given two linked lists, insert nodes of second list into first list at alternate positions of first list.
# For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6, the first list should become 5->12->7->10->17->2->13->4->11->6 and second list should become empty. The nodes of second list should only be inserted when there are positions available. For example, if the first list is 1->2->3 and second list is 4->5->6->7->8, then first list should become 1->4->2->5->3->6 and second list to 7->8.
# 
# Use of extra space is not allowed (Not allowed to create additional nodes), i.e., insertion must be done in-place. Expected time complexity is O(n) where n is number of nodes in first list.

# In[20]:


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def insert_alternate_positions(first_head, second_head):
    if first_head is None:
        return second_head

    first_ptr = first_head
    second_ptr = second_head

    while first_ptr is not None and second_ptr is not None:
        temp = second_ptr.next
        second_ptr.next = first_ptr.next
        first_ptr.next = second_ptr
        first_ptr = second_ptr.next
        second_ptr = temp

    if second_ptr is not None:
        # If second linked list has more nodes, append them to the end of the first linked list
        current = first_head
        while current.next is not None:
            current = current.next
        current.next = second_ptr

    return first_head
# Create the first linked list: 5->7->17->13->11
first_head = Node(5)
first_head.next = Node(7)
first_head.next.next = Node(17)
first_head.next.next.next = Node(13)
first_head.next.next.next.next = Node(11)

# Create the second linked list: 12->10->2->4->6
second_head = Node(12)
second_head.next = Node(10)
second_head.next.next = Node(2)
second_head.next.next.next = Node(4)
second_head.next.next.next.next = Node(6)

# Insert nodes of the second linked list into the first linked list at alternate positions
modified_first_head = insert_alternate_positions(first_head, second_head)

# Print the modified first linked list
current = modified_first_head
while current is not None:
    print(current.data, end="->")
    current = current.next

# Print the second linked list (should be empty)
print(second_head)  # Output: None


# # Question 8
# Given a singly linked list, find if the linked list is circular or not.
# A linked list is called circular if it is not NULL-terminated and all nodes are connected in the form of a cycle. Below is an example of a circular linked list.
# 

# In[21]:


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def is_circular(head):
    if head is None:
        return False

    slow_ptr = head
    fast_ptr = head.next

    while fast_ptr is not None and fast_ptr.next is not None:
        if fast_ptr == slow_ptr or fast_ptr.next == slow_ptr:
            return True
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return False
# Create a circular linked list: 1->2->3->4->5 (the last node points back to the second node)
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next

# Check if the linked list is circular
is_circular_result = is_circular(head)
print(is_circular_result)  # Output: True

# Create a non-circular linked list: 1->2->3->4->5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Check if the linked list is circular
is_circular_result = is_circular(head)
print(is_circular_result)  # Output: False


# In[ ]:




