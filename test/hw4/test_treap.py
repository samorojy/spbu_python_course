import pytest

from src.hw4.treap import Treap, TreapNode, merge, split


def test_treap_insert():
    tree = Treap({0: "a", 1: "b", 2: "c", 3: "d"})
    tree[4] = "Kotlin"
    assert tree[4].value == "Kotlin"


def test_treap_remove():
    tree = Treap({0: "a", 1: "b", 2: "c", 3: "d"})
    del tree[1]
    with pytest.raises(KeyError):
        var = tree[1]
    with pytest.raises(KeyError):
        del tree[5]


def test_treap_find_node():
    tree = Treap({0: "a", 1: "b", 2: "c", 3: "d"})
    assert tree.find_node(0).value == "a"


def test_treap_merge():
    first_tree = Treap({10: "Ocaml", 20: "Magenta"})
    second_tree = Treap({80: "CodeTracker", 90: "Bebroo"})
    merge_result = merge(first_tree.root, second_tree.root)
    treap = Treap({})
    treap.insert(merge_result)
    assert treap.find_node(10).value == "Ocaml"
    assert treap.find_node(90).value == "Bebroo"


def test_treap_split():
    tree = Treap({0: "a", 1: "b", 2: "c", 3: "d"})
    tree.insert(TreapNode(12, "Kotlin"))
    less, bigger, equals = split(tree.root, 3)
    less_tree = Treap({})
    less_tree.insert(less)
    bigger_tree = Treap({})
    bigger_tree.insert(bigger)
    assert less_tree.find_node(0).value == "a"
    assert bigger_tree.find_node(12).value == "Kotlin"
    assert equals.value == "d"


def test_treap_pop():
    tree = Treap({0: "a", 1: "b", 2: "c", 3: "d"})
    tree.pop(1)
    with pytest.raises(KeyError):
        var = tree[1]
