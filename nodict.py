#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'aradcliff'


class Node:
    def __init__(self, key, value=None):
        self.hash = None
        self.key = key
        self.value = value
        self.hash = hash(self.key)

    def __repr__(self):
        """Representation of key/value contents"""
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """Equal operator"""
        return True if self.key == other.key else False


class NoDict:
    def __init__(self, num_buckets=10):
        self.buckets = [[] for i in range(num_buckets)]

    def __repr__(self):
        """Return a string representing the NoDict contents"""
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        """Store new key/value into NoDict instance"""
        new_node = Node(key, value)
        index = new_node.hash % len(self.buckets)
        for node in self.buckets[index]:
            if node == new_node:
                self.buckets[index].remove(node)
        self.buckets[index].append(new_node)

    def get(self, key):
        # Your code here
        return

    def __getitem__(self, key):
        # Your code here
        return

    def __setitem__(self, key, value):
        # Your code here
        return
