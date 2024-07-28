#Discrete Structure (CSCI 220)
#July 2024
#Assignment 9 - Trees and Tree Algorithms
#Yutong Ye

import Assignment08 as as8
import random


COUNT = [10]
def print_2d_util(root, space):
    if root == None:
        return
    space += COUNT[0]
    print_2d_util(root.right, space)
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.val)
    print_2d_util(root.left, space)


def print_2d(root):
    print_2d_util(root, 0)


# Wrapper over print2DUtil()


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to insert a new node with the given key
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root



#[1] Declare a variable size and assign it a number, e.g. 100. Build a list of numbers between 1 and size, and then shuffle the numbers into a random permutation. We will refer to this list as the "keys".
def ordered_keys(size):
    keys = [i for i in range(1, size+1)]
    return keys


def random_keys(size):
    keys = ordered_keys(size)
    random.shuffle(keys)
    return keys


def inorder_rec(root, result):
    if root:
        inorder_rec(root.left, result)
        result.append(root.val)
        inorder_rec(root.right, result)
    return result


def inorder(root):
    result = []
    return inorder_rec(root, result)


def preorder(root):
    result = []
    return preorder_rec(root, result)


def preorder_rec(root, result):
    if root:
        result.append(root.val)
        preorder_rec(root.left, result)
        preorder_rec(root.right, result)
    return result


def postorder(root):
    result = []
    return postorder_rec(root, result)


def postorder_rec(root, result):
    if root:
        postorder_rec(root.left, result)
        postorder_rec(root.right, result)
        result.append(root.val)
    return result


def reverse_order(root):
    result = []
    return reverse_order_rec(root, result)


def reverse_order_rec(root, result):
    if root:
        reverse_order_rec(root.right, result)
        result.append(root.val)
        reverse_order_rec(root.left, result)
    return result


def height(root):
    if not root:
        return -1;
    else:
        return max(height(root.left), height(root.right)) + 1


def num_keys(root):
    if not root:
        return 0
    else:
        return num_keys(root.left) + num_keys(root.right) + 1


def sum_keys(root):
    if not root:
        return 0
    else:
        return sum_keys(root.left) + sum_keys(root.right) + root.val


def min_keys(root):
    if not root.left:
        return root.val
    else:
        return min_keys(root.left)


def max_keys(root):
    if not root.right:
        return root.val
    else:
        return min_keys(root.right)


def level_order(root):
    h = height(root)
    results = []
    for i in range(1, h+1):
        current_level(root, i, results)
    return results


# Print nodes at a current level
def current_level(root, level, results):
    if root is None:
        return
    if level == 1:
        results.append(root.val)
    elif level > 1:
        current_level(root.left, level-1, results)
        current_level(root.right, level-1, results)


def leaves(root):
    result = []
    leaves_rec(root, result)
    return result


def leaves_rec(root, result):
    if not root:
        return
    elif not root.left and not root.right:
        result.append(root.val)
    elif root.left:
        leaves_rec(root.left, result)
    if root.right:
        leaves_rec(root.right, result)


def root_node(root):
    return root.val


#[2] Define a function build_tree(keys) that builds a binary search tree by starting with a root node with key key[0] and gradually inserts the remaining keys following the BST property (smaller on the left, larger on the right). We will use a simple list as a node, in which node[0] is the key, node[1] is the left subtree (LST), and node[2] is the right subtree (RST).
def build_tree(keys):
    root = Node(keys[0])
    for key in keys[1:]:
        root = insert(root, key)
    return root


def do_tree_properties(title, root, properties):
    headers = ["Property", "Value"]
    data = [[prop.__name__, prop(root)] for prop in properties]
    alignments = ['l', 'l']
    as8.print_table(title, headers, data, alignments)


def main():
    keys = random_keys(20)
    print(keys)
    root = build_tree(keys)
    properties = [height, num_keys, sum_keys, root_node, min_keys,max_keys, leaves, inorder, preorder, postorder, reverse_order, level_order]
    do_tree_properties("Tree Properties", root, properties)


if __name__ == '__main__':
    main()