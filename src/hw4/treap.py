import random


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


class Treap:
    """
    Data structure combining the properties of a binary tree and a heap
    """

    def __init__(self, nodes: dict):
        self.root = None
        self.size = 0
        for key in nodes:
            self.root = Treap.insert(self.root, TreapNode(key, nodes[key]))
            self.size += 1

    def __setitem__(self, key, value):
        Treap.insert(self.root, TreapNode(key, value))

    def __getitem__(self, item):
        find_result = Treap.find_node(self.root, item)
        if find_result is None:
            raise KeyError(f"There is no key: {item} in the three")
        return find_result

    def __delitem__(self, key):
        self.root = Treap.remove(self.root, key)

    def __contains__(self, item):
        return Treap.find_node(self.root, item) is not None

    def __str__(self):
        return str(self.root)

    def __iter__(self):
        yield from self.root.__iter__()

    @staticmethod
    def insert(source_node: TreapNode, node_to_insert: TreapNode) -> TreapNode:
        """
        Appends a new node to the tree

        :param source_node: root of the tree
        :param node_to_insert: node to append
        :return: new root of the tree
        """
        if source_node is None:
            return node_to_insert
        temp_node = Treap.split(source_node, node_to_insert.key)
        return Treap.merge(Treap.merge(temp_node[0], node_to_insert), temp_node[1])

    @staticmethod
    def remove(source_node: TreapNode, value_to_remove) -> TreapNode:
        """
        Removes value from the tree

        :param source_node: root of the tree
        :param value_to_remove: value to be removed
        :return: new root of the tree
        """
        temp_node = Treap.split(source_node, value_to_remove)
        return Treap.merge(temp_node[1], temp_node[2])

    @staticmethod
    def find_node(source_node: TreapNode, key):
        """
        Finds the value of the node with the given key

        :param source_node: root of the tree
        :param key: key of node to find
        :return: value of node with passed key or None
        """
        if source_node is None:
            return None
        if source_node.key == key:
            return source_node.value
        if source_node.key > key:
            return Treap.find_node(source_node.left_child, key)
        else:
            return Treap.find_node(source_node.right_child, key)

    @staticmethod
    def split(node: TreapNode, split_key) -> tuple:
        """
        Splits a tree by key

        :param node: root of the tree
        :param split_key: key of the node to split
        :return: tuple of (less_keys_tree_root, bigger_keys_tree_root, equals_keys_tree_root)
        """
        if node is None:
            return None, None, None
        if node.key < split_key:
            temp_node = Treap.split(node.right_child, split_key)
            node.right_child = temp_node[0]
            return node, temp_node[1], temp_node[2]
        elif node.key == split_key:
            return node.left_child, node.right_child, node
        else:
            temp_node = Treap.split(node.left_child, split_key)
            node.left_child = temp_node[1]
            return temp_node[0], node, temp_node[2]

    @staticmethod
    def merge(less_keys_tree: TreapNode, bigger_keys_tree: TreapNode) -> TreapNode:
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
            less_keys_tree.right_child = Treap.merge(less_keys_tree.right_child, bigger_keys_tree)
            return less_keys_tree
        else:
            bigger_keys_tree.left_child = Treap.merge(less_keys_tree, bigger_keys_tree.left_child)
            return bigger_keys_tree
