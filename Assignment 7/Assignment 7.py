#!/usr/bin/env python3
"""
bst_operations.py

Binary Search Tree (BST) implementation with:
 - InsertBST(x, T): inserts integer x into BST T, returns 1 if inserted, 0 if already present
 - DeleteBST(x, T): deletes integer x from BST T, returns 1 if deleted, 0 if not found
"""

class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def InsertBST(self, x: int) -> int:
        """
        Insert integer x into BST.
        Returns:
            1 if insertion is successful,
            0 if x already exists in the tree.
        """
        def _insert(node, x):
            if node is None:
                return Node(x), True
            if x < node.key:
                node.left, inserted = _insert(node.left, x)
            elif x > node.key:
                node.right, inserted = _insert(node.right, x)
            else:
                # x == node.key; no duplicates
                return node, False
            return node, inserted

        self.root, inserted = _insert(self.root, x)
        return 1 if inserted else 0

    def DeleteBST(self, x: int) -> int:
        """
        Delete integer x from BST.
        Returns:
            1 if deletion is successful,
            0 if x is not found in the tree.
        """
        def _delete(node, x):
            if node is None:
                return node, False
            if x < node.key:
                node.left, deleted = _delete(node.left, x)
                return node, deleted
            if x > node.key:
                node.right, deleted = _delete(node.right, x)
                return node, deleted
            # node.key == x: perform delete
            if node.left is None:
                return node.right, True
            if node.right is None:
                return node.left, True
            # node with two children: find inorder successor
            succ = node.right
            while succ.left:
                succ = succ.left
            node.key = succ.key
            node.right, _ = _delete(node.right, succ.key)
            return node, True

        self.root, deleted = _delete(self.root, x)
        return 1 if deleted else 0

    def inorder(self):
        """Return in-order traversal as a list of keys."""
        result = []
        def _in(node):
            if node:
                _in(node.left)
                result.append(node.key)
                _in(node.right)
        _in(self.root)
        return result

def main():
    # Create BST instance
    bst = BST()

    # Insert sample keys
    keys_to_insert = [50, 30, 70, 20, 40, 60, 80]
    print("== Inserting keys ==")
    for key in keys_to_insert:
        status = bst.InsertBST(key)
        print(f"Insert {key}: {'Success' if status == 1 else 'Already exists'}")

    print("\nIn-order after insertions:", bst.inorder())

    # Attempt to insert duplicate
    dup_key = 30
    status = bst.InsertBST(dup_key)
    print(f"\nInsert {dup_key} again: {'Success' if status == 1 else 'Already exists'}")

    # Delete keys (leaf, one child, two children, non-existent)
    for del_key in [20, 30, 50, 100]:
        status = bst.DeleteBST(del_key)
        print(f"\nDelete {del_key}: {'Success' if status == 1 else 'Not found'}")
        print("In-order now:", bst.inorder())

if __name__ == "__main__":
    main()
