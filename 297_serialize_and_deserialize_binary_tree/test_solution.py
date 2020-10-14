from solution import CodecPreOrder, TreeNode, CodecPostOrder, CodecLevelOrder
import pytest
import pudb


@pytest.fixture
def tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    return root


def test_pre_order(tree):
    ser = CodecPreOrder().serialize(tree)
    assert ser == ",".join(str(e)
                           for e in [1, 2, '#', '#', 3, 4, '#', '#', 5, '#', '#'])
    # pudb.set_trace()
    root = CodecPreOrder().deserialize(ser)
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 3
    assert root.right.left.val == 4
    assert root.right.right.val == 5


def test_post_order(tree):
    ser = CodecPostOrder().serialize(tree)
    assert ser == '#,#,2,#,#,4,#,#,5,3,1'
    # pudb.set_trace()
    root = CodecPostOrder().deserialize(ser)
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 3
    assert root.right.left.val == 4
    assert root.right.right.val == 5


def test_level_order(tree):
    # pudb.set_trace()
    ser = CodecLevelOrder().serialize(tree)
    assert ser == '1,2,3,#,#,4,5,#,#,#,#'
    root = CodecLevelOrder().deserialize(ser)
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 3
    assert root.right.left.val == 4
    assert root.right.right.val == 5
