class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_close(root, k):
    dist = [(None, float('inf')), (None, float('inf')), None]
    height(root, dist, False, 0, k)

    if dist[0][1] - dist[2] > dist[1][1] + dist[2]:
        return dist[1][0]
    else:
        return dist[0][0]


"""
This does not work for the following case:
            1
          /   \
         4     3
        / \
       5   7
      /
     6
    /
   8
    \
     9
target = 5, this method only record 9, 3. However the right result is 7.


"""


def height(root, dist, met_target, pre_h, target):
    """
    dist is a list of two elements, dist[0] shortest node that contains target,
    dist[1] shortest node that does not contain target.
    """
    if not root:
        return
    if root.val == target:
        dist[2] = pre_h + 1
        met_target = True
    if not root.left and not root.right:
        if met_target:
            if dist[0][1] > pre_h + 1:
                dist[0] = (root.val, pre_h + 1)
        else:
            if dist[1][1] > pre_h + 1:
                dist[1] = (root.val, pre_h + 1)
    height(root.left, dist, met_target, pre_h+1, target)
    height(root.right, dist, met_target, pre_h + 1, target)

