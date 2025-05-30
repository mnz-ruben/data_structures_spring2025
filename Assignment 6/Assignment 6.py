#!/usr/bin/env python3
"""
hash_table.py

A simple hash table implementation using linear probing.
Supports integer keys with:
 - HashInsertion(key): insert key, return index or -1 if full
 - HashDeletion(key): delete key, return index or -1 if not found
"""

class HashTable:
    def __init__(self, size=907):
        self.size = size
        self.table = [None] * size
        # Tombstone marker for deleted slots
        self.DELETED = object()

    def _hash(self, key: int) -> int:
        """Primary hash: key mod table size."""
        return key % self.size

    def HashInsertion(self, key: int) -> int:
        """
        Insert `key` into the table.
        Returns the index where inserted, or -1 if the table is full.
        """
        for i in range(self.size):
            idx = (self._hash(key) + i) % self.size
            if self.table[idx] is None or self.table[idx] is self.DELETED:
                self.table[idx] = key
                return idx
        return -1  # table full

    def HashDeletion(self, key: int) -> int:
        """
        Delete `key` from the table (marks it deleted).
        Returns the index where deleted, or -1 if the key was not found.
        """
        for i in range(self.size):
            idx = (self._hash(key) + i) % self.size
            if self.table[idx] == key:
                self.table[idx] = self.DELETED
                return idx
            if self.table[idx] is None:
                # Stop searching on an empty slot
                break
        return -1  # key not found

    def __str__(self) -> str:
        """Printable representation of the underlying array."""
        return str(self.table)

def main():
    # For demonstration, use a small table for clarity
    ht = HashTable(size=7)

    # 1) Insert a few keys
    print("== Inserting keys ==")
    for key in [10, 3, 17, 24]:
        idx = ht.HashInsertion(key)
        print(f"Insert {key} -> index {idx}")

    # 2) Show current table
    print("\nTable state:", ht)

    # 3) Insert another key to demonstrate collision resolution
    extra = 31
    idx = ht.HashInsertion(extra)
    print(f"\nInsert {extra} -> index {idx}")
    print("Table state:", ht)

    # 4) Delete an existing key
    to_del = 17
    idx = ht.HashDeletion(to_del)
    print(f"\nDelete {to_del} -> index {idx}")
    print("Table state:", ht)

    # 5) Attempt to delete a non-existent key
    missing = 99
    idx = ht.HashDeletion(missing)
    print(f"\nDelete {missing} -> index {idx} (not found)")
    print("Final table state:", ht)

if __name__ == "__main__":
    main()
