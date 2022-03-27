import pytest

from src.hw4.treap import Treap, TreapNode


def test_treap():
    tree = Treap({0: "a", 1: "b", 2: "c", 3: "d"})

    def test_insert(key, value):
        tree[key] = value
        assert tree[key] == value

    def test_remove(key):
        del tree[key]
        with pytest.raises(KeyError):
            var = tree[key]

    def test_find_node(key, value):
        assert Treap.find_node(tree.root, key) == value

    def test_split(key, less_key, less_value, bigger_key, bigger_value):
        split_result = tree.split(tree.root, key)
        assert Treap.find_node(split_result[0], less_key) == less_value
        assert Treap.find_node(split_result[1], bigger_key) == bigger_value

    def test_merge(
        less_keys_tree_root,
        bigger_keys_tree_root,
        less_branch_element_key,
        less_branch_element_value,
        bigger_branch_element_key,
        bigger_branch_element_value,
    ):
        merge_result = Treap.merge(less_keys_tree_root, bigger_keys_tree_root)
        assert Treap.find_node(merge_result, less_branch_element_key) == less_branch_element_value
        assert Treap.find_node(merge_result, bigger_branch_element_key) == bigger_branch_element_value

    test_insert(4, "Python")
    test_insert(12, "Kotlin")
    test_remove(1)
    test_find_node(3, "d")
    test_find_node(228, None)
    test_split(3, 0, "a", 12, "Kotlin")

    less_keys_branch_root = Treap.insert(TreapNode(10, "OCaml"), TreapNode(20, "Magenta"))
    bigger_keys_branch_root = Treap.insert(TreapNode(80, "CodeTracker"), TreapNode(90, "Bebroo"))
    test_merge(less_keys_branch_root, bigger_keys_branch_root, 10, "OCaml", 90, "Bebroo")

    def test_size(size: int):
        assert len(tree) == size

    test_size(5)
    tree.popitem()
    test_size(4)
