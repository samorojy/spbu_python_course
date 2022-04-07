import random
from collections.abc import MutableMapping
from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class TreapNode:
    """
    Treap element
    """

    def __init__(self, key, value):
        self.key = key
        self.priority = random.randint(0, 100)
        self.value = value
        self.left_child = None
        self.right_child = None

    def __iter__(self):
        if self.left_child is not None:
            for node in self.left_child:
                yield node
        yield self
        if self.right_child is not None:
            for node in self.right_child:
                yield node

    def __repr__(self):
        return f"<{self.key}:{self.value}, left: {self.left_child}, right: {self.right_child}>"


class Treap(MutableMapping):
    """
    Data structure combining the properties of a binary tree and a heap
    """

    def __init__(self, nodes: dict):
        self.root: Optional[TreapNode] = None
        self._size = len(nodes)
        for key in nodes:
            self.insert(TreapNode(key, nodes[key]))

    def __setitem__(self, key, value):
        self.insert(TreapNode(key, value))

    def __getitem__(self, item):
        find_result = self.find_node(item)
        if find_result is None:
            raise KeyError(f"There is no key: {item} in the tree")
        return find_result

    def __delitem__(self, key):
        self.remove(key)

    def __contains__(self, item):
        return self.find_node(item) is not None

    def __str__(self):
        return str(self.root)

    def __len__(self):
        return self._size

    def __iter__(self):
        for node in self.root:
            yield node.key

    def clear(self):
        self._size = 0
        self.root = None

    def insert(self, node_to_insert: TreapNode):
        """
        Appends a new node to the tree

        :param node_to_insert: node to append
        :return: new root of the tree
        """
        if self.root is None:
            self.root = node_to_insert
            self._size += 1
        else:
            less, bigger, equals = split(self.root, node_to_insert.key)
            if equals is None:
                self._size += 1
            self.root = merge(merge(less, node_to_insert), bigger)

    def remove(self, key_to_remove) -> TreapNode:
        """
        Removes value from the tree

        :param key_to_remove: value to be removed
        :return: new root of the tree
        """
        less, bigger, equals = split(self.root, key_to_remove)
        if equals is None:
            raise KeyError("Node with this key does not exist in the Treap")
        self.root = merge(less, bigger)
        return equals

    def find_node(self, key) -> Optional[TreapNode]:
        """
        Finds the value of the node with the given key

        :param key: key of node to find
        :return: value of node with passed key or None
        """
        current_node = self.root
        while current_node is not None:
            if current_node.key == key:
                return current_node
            if current_node.key < key:
                current_node = current_node.right_child
            else:
                current_node = current_node.left_child
        return None


def split(node: Optional[TreapNode], split_key) -> Tuple:
    """
    Splits a tree by key

    :param node: root of the tree
    :param split_key: key of the node to split
    :return: tuple of (less_keys_tree_root, bigger_keys_tree_root, equals_keys_tree_root)
    """
    if node is None:
        return None, None, None
    if node.key < split_key:
        temp_node = split(node.right_child, split_key)
        node.right_child = temp_node[0]
        return node, temp_node[1], temp_node[2]
    elif node.key == split_key:
        return node.left_child, node.right_child, node
    else:
        temp_node = split(node.left_child, split_key)
        node.left_child = temp_node[1]
        return temp_node[0], node, temp_node[2]


def merge(less_keys_tree: Optional[TreapNode], bigger_keys_tree: Optional[TreapNode]) -> Optional[TreapNode]:
    """
    Merges two parts of trees

    :param less_keys_tree: root of the less keys tree
    :param bigger_keys_tree: root of the bigger keys tree
    :return: new root of the tree
    """
    if less_keys_tree is None:
        return bigger_keys_tree
    if bigger_keys_tree is None:
        return less_keys_tree
    if less_keys_tree.priority > bigger_keys_tree.priority:
        less_keys_tree.right_child = merge(less_keys_tree.right_child, bigger_keys_tree)
        return less_keys_tree
    else:
        bigger_keys_tree.left_child = merge(less_keys_tree, bigger_keys_tree.left_child)
        return bigger_keys_tree
