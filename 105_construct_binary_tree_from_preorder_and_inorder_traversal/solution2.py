from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self._build_tree(preorder, inorder)

    def _build_tree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        preorder_left = preorder[1:root_index+1]
        preorder_right = preorder[root_index+1:]
        inorder_left = inorder[:root_index]
        inorder_right = inorder[root_index+1:]

        root.left = self._build_tree(preorder_left, inorder_left)
        root.right = self._build_tree(preorder_right, inorder_right)

        return root


"""
pre = [3, 9, 20, 15, 7], in = [9, 3, 15, 20, 7]
root = 3
root = 3, root_index = 1, pre_left = [9], pre_right = [20, 15, 7], in_left = [9], in_right = [15, 20, 7]

    bt([9], [9]):
        root = 9, root_index = 0
    done

    bt([20, 15, 7], [15, 20, 7])
        root = 20, root_index = 1, pre_left = [15], pre_right = [7], in_left = [15], in_right = [7]

    done
"""
