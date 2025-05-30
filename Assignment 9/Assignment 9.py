#!/usr/bin/env python3
"""
b_minus_tree.py

ADT for a B-Tree ("B-") with insert operation.

Functions:
 - insetBminustree(key, tree): inserts key into the B-Tree, returns 1 on success.
Usage:
    tree = BMinusTree(t)
    status = insetBminustree(key, tree)
"""

class BMinusTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t                 # minimum degree
        self.keys = []             # keys in node
        self.children = []         # child pointers
        self.leaf = leaf           # True if leaf

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BMinusTreeNode(t, leaf=y.leaf)
        # move last t-1 keys of y to z
        z.keys = y.keys[t:]
        if not y.leaf:
            z.children = y.children[t:]
        # reduce y
        y.keys = y.keys[:t-1]
        if not y.leaf:
            y.children = y.children[:t]
        # insert new child
        self.children.insert(i+1, z)
        # move median key up
        median = y.keys.pop(-1)
        self.keys.insert(i, median)

    def insert_nonfull(self, key):
        i = len(self.keys) - 1
        if self.leaf:
            # insert key into correct position
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i+1] = self.keys[i]
                i -= 1
            self.keys[i+1] = key
        else:
            # find child to descend
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            # split full child
            if len(self.children[i].keys) == 2*self.t - 1:
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_nonfull(key)

class BMinusTree:
    def __init__(self, t):
        self.t = t
        self.root = BMinusTreeNode(t, leaf=True)

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2*self.t - 1:
            new_root = BMinusTreeNode(self.t, leaf=False)
            new_root.children.append(root)
            new_root.split_child(0)
            self.root = new_root
            self.root.insert_nonfull(key)
        else:
            root.insert_nonfull(key)
        return 1

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, "Keys:", node.keys)
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level+1)

def insetBminustree(key, tree):
    return tree.insert(key)

def main():
    btree = BMinusTree(t=2)
    keys = [10, 20, 5, 6, 12, 30, 7, 17]
    print("== Inserting keys into B-Tree ==")
    for key in keys:
        status = insetBminustree(key, btree)
        print(f"Insert {key}: {'Success' if status == 1 else 'Fail'}")

    print("\nB-Tree structure:")
    btree.print_tree()

if __name__ == "__main__":
    main()
