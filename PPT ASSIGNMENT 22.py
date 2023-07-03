#!/usr/bin/env python
# coding: utf-8

# # Question-1:
# Given a Binary Tree (Bt), convert it to a Doubly Linked List(DLL). The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be the same as in Inorder for the given Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.
# 

# In[1]:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def convertToDLL(root):
    global prev

    if root is None:
        return

    convertToDLL(root.left)

    root.right = prev

    if prev is not None:
        prev.left = root

    prev = root

    convertToDLL(root.right)


def convertBinaryTreeToDLL(root):
    global prev
    prev = None

    convertToDLL(root)

    head = prev
    while head and head.left:
        head = head.left

    return head


# # Question-2
# A Given a binary tree, the task is to flip the binary tree towards the right direction that is clockwise. See the below examples to see the transformation.
# In the flip operation, the leftmost node becomes the root of the flipped tree and its parent becomes its right child and the right sibling becomes its left child and the same should be done for all left most nodes recursively.
# 

# In[2]:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def flipBinaryTree(root):
    if root is None or (root.left is None and root.right is None):
        return root

    newRoot = flipBinaryTree(root.left)

    root.left = None
    root.right = flipBinaryTree(root.right)

    if newRoot:
        temp = newRoot
        while temp.right:
            temp = temp.right
        temp.right = root

    return newRoot


def printInorder(root):
    if root is None:
        return

    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)


# Example usage:
# Create a binary tree
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Original Tree:")
printInorder(root)

flippedRoot = flipBinaryTree(root)

print("\nFlipped Tree:")
printInorder(flippedRoot)


# # Question-3:
# Given a binary tree, print all its root-to-leaf paths without using recursion. For example, consider the following Binary Tree.
# 

# In[4]:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printRootToLeafPaths(root):
    if root is None:
        return

    stack = [(root, [])]  # (node, current path)
    paths = []

    while stack:
        node, path = stack.pop()

        # Leaf node, add current path to paths
        if node.left is None and node.right is None:
            paths.append(path + [node.data])

        if node.right:
            stack.append((node.right, path + [node.data]))

        if node.left:
            stack.append((node.left, path + [node.data]))

    # Print all paths
    for path in paths:
        print("->".join(map(str, path)))


# Example usage:
# Create a binary tree
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Root-to-leaf paths:")
printRootToLeafPaths(root)


# # Question-4:
# Given Preorder, Inorder and Postorder traversals of some tree. Write a program to check if they all are of the same tree.
# 

# In[5]:


def isSameTree(preorder, inorder, postorder):
    if not preorder and not inorder and not postorder:
        return True

    if len(preorder) != len(inorder) or len(preorder) != len(postorder) or len(inorder) != len(postorder):
        return False

    if preorder[0] != postorder[-1]:
        return False

    root = preorder[0]
    rootIndex = inorder.index(root)

    leftPreorder = preorder[1:rootIndex + 1]
    leftInorder = inorder[:rootIndex]
    leftPostorder = postorder[:rootIndex]

    rightPreorder = preorder[rootIndex + 1:]
    rightInorder = inorder[rootIndex + 1:]
    rightPostorder = postorder[rootIndex:-1]

    return isSameTree(leftPreorder, leftInorder, leftPostorder) and isSameTree(rightPreorder, rightInorder, rightPostorder)


# Example usage:
preorder = [1, 2, 4, 5, 3, 6, 7]
inorder = [4, 2, 5, 1, 6, 3, 7]
postorder = [4, 5, 2, 6, 7, 3, 1]

print("Are the traversals of the same tree?", isSameTree(preorder, inorder, postorder))

