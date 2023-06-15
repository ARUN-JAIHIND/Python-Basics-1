#!/usr/bin/env python
# coding: utf-8

# # Question 1
# Given two linked list of the same size, the task is to create a new linked list using those linked lists. The condition is that the greater node among both linked list will be added to the new linked list.
# 

# In[5]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_lists(list1, list2):
    # Create a new empty linked list
    newList = None

    # Traverse both linked lists simultaneously
    while list1 is not None and list2 is not None:
        # Compare the values of the nodes
        if list1.data >= list2.data:
            # Add the node from list1 to the new list
            newNode = Node(list1.data)
            newNode.next = newList
            newList = newNode
            list1 = list1.next
        else:
            # Add the node from list2 to the new list
            newNode = Node(list2.data)
            newNode.next = newList
            newList = newNode
            list2 = list2.next

    # Add remaining nodes from list1, if any
    while list1 is not None:
        newNode = Node(list1.data)
        newNode.next = newList
        newList = newNode
        list1 = list1.next

    # Add remaining nodes from list2, if any
    while list2 is not None:
        newNode = Node(list2.data)
        newNode.next = newList
        newList = newNode
        list2 = list2.next

    return newList

# Helper function to print the linked list
def print_list(head):
    while head is not None:
        print(head.data, end="->")
        head = head.next
    print("None")

# Example usage:
# Creating the first linked list: 5->2->3->8
list1 = Node(5)
list1.next = Node(2)
list1.next.next = Node(3)
list1.next.next.next = Node(8)

# Creating the second linked list: 1->7->4->5
list2 = Node(1)
list2.next = Node(7)
list2.next.next = Node(4)
list2.next.next.next = Node(5)

# Merge the two linked lists
newList = merge_lists(list1, list2)

# Print the merged linked list
print_list(newList)


# # Question 2
# Write a function that takes a list sorted in non-decreasing order and deletes any duplicate nodes from the list. The list should only be traversed once.
# For example if the linked list is 11->11->11->21->43->43->60 then removeDuplicates() should convert the list to 11->21->43->60.
# 

# In[6]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    current = head

    # Traverse the list
    while current is not None and current.next is not None:
        # Compare current node with the next node
        if current.data == current.next.data:
            # Skip the next node by updating current's next pointer
            current.next = current.next.next
        else:
            # Move to the next node
            current = current.next

    return head

# Helper function to print the linked list
def print_list(head):
    while head is not None:
        print(head.data, end="->")
        head = head.next
    print("None")

# Example usage:
# Creating the linked list: 11->11->11->21->43->43->60
head = Node(11)
head.next = Node(11)
head.next.next = Node(11)
head.next.next.next = Node(21)
head.next.next.next.next = Node(43)
head.next.next.next.next.next = Node(43)
head.next.next.next.next.next.next = Node(60)

# Remove duplicates from the linked list
head = remove_duplicates(head)

# Print the modified linked list
print_list(head)


# # Question 3
# Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should be considered as a group and must be reversed (See Example 2 for clarification).
# 

# In[7]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_k_nodes(head, k):
    prev = None
    curr = head
    next = None
    count = 0

    # Reverse the group of k nodes
    while curr is not None and count < k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1

    # Recursively reverse the next group of k nodes
    if next is not None:
        head.next = reverse_k_nodes(next, k)

    return prev

# Helper function to print the linked list
def print_list(head):
    while head is not None:
        print(head.data, end="->")
        head = head.next
    print("None")

# Example usage:
# Creating the linked list: 1->2->3->4->5->6->7->8->9
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)

k = 3  # Number of nodes to reverse

# Reverse every k nodes in the linked list
head = reverse_k_nodes(head, k)

# Print the modified linked list
print_list(head)


# # Question 4
# Given a linked list, write a function to reverse every alternate k nodes (where k is an input to the function) in an efficient way. Give the complexity of your algorithm.
# 
# 

# In[8]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_alternate_k_nodes(head, k):
    prev = None
    curr = head
    next = None
    count = 0
    is_alternate = True
    alternate_head = None
    alternate_tail = None
    prev_tail = None

    # Reverse the alternate groups of k nodes
    while curr is not None:
        while curr is not None and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        if is_alternate:
            if alternate_head is None:
                alternate_head = prev
                alternate_tail = prev
            else:
                alternate_tail.next = prev
                alternate_tail = prev
            is_alternate = False
        else:
            if prev_tail is None:
                head = prev
            else:
                prev_tail.next = prev
            prev_tail = alternate_tail
            alternate_head = None
            is_alternate = True

        if count < k:
            break

        prev = None
        count = 0

    if alternate_head is not None:
        prev_tail.next = alternate_head

    return head

# Helper function to print the linked list
def print_list(head):
    while head is not None:
        print(head.data, end="->")
        head = head.next
    print("None")

# Example usage:
# Creating the linked list: 1->2->3->4->5->6->7->8->9->10
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

k = 3  # Number of nodes to reverse altern


# # Question 5
# Given a linked list and a key to be deleted. Delete last occurrence of key from linked. The list may have duplicates.
# 

# In[13]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_last_occurrence(head, key):
    prev = None
    curr = None
    key_found = False

    # Traverse the linked list
    temp = head
    while temp is not None:
        if temp.data == key:
            prev = curr
            curr = temp
            key_found = True
        temp = temp.next

    # Check if key was found
    if not key_found:
        return head

    # Perform the deletion
    if curr == head:
        head = curr.next
    else:
        prev.next = curr.next

    return head

# Helper function to print the linked list
def print_list(head):
    while head is not None:
        print(head.data, end="->")
        head = head.next
    print("None")

# Example usage:
# Creating the linked list: 1->2->3->2->4->2->5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next = Node(5)

key = 2  # Key to be deleted

# Delete the last occurrence of the key
head = delete_last_occurrence(head, key)

# Print the modified linked list
print_list(head)


# # Question 6
# Given two sorted linked lists consisting of N and M nodes respectively. The task is to merge both of the lists (in place) and return the head of the merged list.
# 
# 

# In[14]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sorted_lists(head1, head2):
    dummy = Node(0)
    curr = dummy

    # Traverse both lists simultaneously
    ptr1 = head1
    ptr2 = head2
    while ptr1 is not None and ptr2 is not None:
        if ptr1.data <= ptr2.data:
            curr.next = ptr1
            ptr1 = ptr1.next
        else:
            curr.next = ptr2
            ptr2 = ptr2.next
        curr = curr.next

    # Append any remaining nodes
    if ptr1 is not None:
        curr.next = ptr1
    if ptr2 is not None:
        curr.next = ptr2

    return dummy.next

# Helper function to print the linked list
def print_list(head):
    while head is not None:
        print(head.data, end="->")
        head = head.next
    print("None")

# Example usage:
# Creating the first linked list: 1->3->5->7
head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)
head1.next.next.next = Node(7)

# Creating the second linked list: 2->4->6
head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)

# Merge the two sorted linked lists
merged_head = merge_sorted_lists(head1, head2)

# Print the merged linked list
print_list(merged_head)


# # Question 7
# Given a Doubly Linked List, the task is to reverse the given Doubly Linked List.
# 
# 

# In[15]:


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def reverse_doubly_linked_list(head):
    prev = None
    curr = head

    # Reverse the doubly linked list
    while curr is not None:
        next = curr.next
        curr.next = prev
        curr.prev = next
        prev = curr
        curr = next

    # Update the head of the doubly linked list
    head = prev

    return head

# Helper function to print the doubly linked list in both forward and backward directions
def print_list(head):
    # Forward traversal
    while head is not None:
        print(head.data, end="->")
        head = head.next
    print("None")

    # Backward traversal
    while head is not None:
        print(head.data, end="->")
        head = head.prev
    print("None")

# Example usage:
# Creating the doubly linked list: 1<->2<->3<->4<->5
head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next
head.next.next.next = Node(4)
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(5)
head.next.next.next.next.prev = head.next.next.next

# Reverse the doubly linked list
head = reverse_doubly_linked_list(head)

# Print the modified doubly linked list
print_list(head)


# # Question 8
# Given a doubly linked list and a position. The task is to delete a node from given position in a doubly linked list.
# 

# In[16]:


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def delete_node_at_position(head, position):
    if head is None:
        return

    if position == 0:
        if head.next is not None:
            head.next.prev = None
        head = head.next
        return head

    curr = head
    count = 0
    while curr is not None and count < position:
        curr = curr.next
        count += 1

    if curr is None:
        return

    curr.prev.next = curr.next
    if curr.next is not None:
        curr.next.prev = curr.prev

    del curr

    return head

# Helper function to print the doubly linked list
def print_list(head):
    while head is not None:
        print(head.data, end="->")
        head = head.next
    print("None")

# Example usage:
# Creating the doubly linked list: 1<->2<->3<->4<->5
head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next
head.next.next.next = Node(4)
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(5)
head.next.next.next.next.prev = head.next.next.next

position = 2  # Position of the node to be deleted

# Delete the node at the given position
head = delete_node_at_position(head, position)

# Print the modified doubly linked list
print_list(head)


# In[ ]:




