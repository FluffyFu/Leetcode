from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    The worst case could be O(n**2) when the tree only has left children. In this case, to find the
    parent index in inorder takes O(n).
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if (not preorder) or (not inorder):
            return None
        root = TreeNode(preorder[0])

        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                break
        left_preoder = preorder[1:i+1]
        left_inorder = inorder[:i]
        right_preoder = preorder[i+1:]
        right_inorder = inorder[i+1:]

        root.left = self.buildTree(left_preoder, left_inorder)
        root.right = self.buildTree(right_preoder, right_inorder)

        return root


class Solution2:
    """
    Build a map to store the index of all the elements in inorder list. The solution becomes O(n) but
    it also take O(n) extra space.
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_map = {}
        inorder_map = {val: i for i, val in enumerate(inorder)}

        return self._build_tree(0, len(preorder)-1, 0, len(inorder)-1, inorder_map, preorder, inorder)

    def _build_tree(self, pre_low, pre_high, in_low, in_high, inorder_map, preorder, inorder) -> TreeNode:
        if pre_low > pre_high or in_low > in_high:
            return None

        root = TreeNode(preorder[pre_low])
        i = inorder_map[preorder[pre_low]]

        root.left = self._build_tree(
            pre_low+1, i, in_low, i-1, inorder_map, preorder, inorder)
        root.right = self._build_tree(
            i+1, pre_high, i+1, in_high, inorder_map, preorder, inorder)

        return root
