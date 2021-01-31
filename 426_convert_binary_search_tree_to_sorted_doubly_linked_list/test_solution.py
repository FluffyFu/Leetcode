from solution import inorder, Node, inorder_dfs


def test_inorder():
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    res = inorder(root)
    assert res == [1, 2, 3, 4, 5]


def test_inorder_dfs():
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    res = inorder_dfs(root)
    assert res == [1, 2, 3, 4, 5]

