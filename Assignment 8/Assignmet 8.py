#!/usr/bin/env python3
"""
tree_rotations.py

Implements single left and right rotations on a binary search tree (BST).

Functions:
 - leftrotation(node_key, tree): rotate left at node with key node_key; returns 1 on success, 0 otherwise.
 - rightrotation(node_key, tree): rotate right at node with key node_key; returns 1 on success, 0 otherwise.

Includes a simple demonstration in main().
"""

class TreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, x: int) -> int:
        """Insert integer x into the BST. Returns 1 if inserted, 0 if already exists."""
        def _insert(node, x):
            if node is None:
                return TreeNode(x), True
            if x < node.key:
                node.left, inserted = _insert(node.left, x)
            elif x > node.key:
                node.right, inserted = _insert(node.right, x)
            else:
                return node, False
            return node, inserted

        self.root, inserted = _insert(self.root, x)
        return 1 if inserted else 0

    def find_with_parent(self, key: int):
        """
        Find the node with `key` and its parent.
        Returns (node, parent) or (None, None) if not found.
        """
        parent = None
        node = self.root
        while node:
            if key < node.key:
                parent = node
                node = node.left
            elif key > node.key:
                parent = node
                node = node.right
            else:
                break
        return node, parent

    def leftrotation(self, key: int) -> int:
        """
        Perform a left rotation at the node with value `key`.
        Returns 1 if successful, 0 if rotation cannot be performed.
        """
        node, parent = self.find_with_parent(key)
        if node is None or node.right is None:
            return 0

        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        if parent is None:
            self.root = new_root
        elif parent.left is node:
            parent.left = new_root
        else:
            parent.right = new_root

        return 1

    def rightrotation(self, key: int) -> int:
        """
        Perform a right rotation at the node with value `key`.
        Returns 1 if successful, 0 if rotation cannot be performed.
        """
        node, parent = self.find_with_parent(key)
        if node is None or node.left is None:
            return 0

        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        if parent is None:
            self.root = new_root
        elif parent.left is node:
            parent.left = new_root
        else:
            parent.right = new_root

        return 1

    def inorder(self) -> list:
        """Return in-order traversal of BST as a list of keys."""
        result = []
        def _in(node):
            if node:
                _in(node.left)
                result.append(node.key)
                _in(node.right)
        _in(self.root)
        return result

def main():
    # Build a sample tree
    bst = BST()
    for k in [20, 10, 30, 5, 15, 25, 35]:
        bst.insert(k)

    print("Initial in-order:", bst.inorder())
    print("Root before rotation:", bst.root.key)

    # Left rotation at 20
    if bst.leftrotation(20):
        print("\nLeft rotation at 20 succeeded")
        print("New in-order:", bst.inorder())
        print("New root:", bst.root.key)
    else:
        print("\nLeft rotation at 20 failed")

    # Right rotation at new root
    root_key = bst.root.key
    if bst.rightrotation(root_key):
        print(f"\nRight rotation at {root_key} succeeded")
        print("New in-order:", bst.inorder())
        print("Root restored to:", bst.root.key)
    else:
        print(f"\nRight rotation at {root_key} failed")

if __name__ == "__main__":
    main()
