def convert(root):
    if not root:
        return root
    head, _ = dfs(root)
    return head


def dfs(root):
    """
    Convert the BTS to DLL() and return its head and tail.
    """
    head, tail = root, root

    if root.left:
        # connect left DLL with root
        lh, lt = dfs(root.left)

        lt.right = root
        root.left = lt
        head = lh

    if root.right:
        # connect right DLL with (left DLL + root)
        rh, rt = dfs(root.right)

        root.right = rh
        rh.left = root
        tail = rt

    # connect the head and tail of DLL
    tail.right = head
    head.left = tail

    return head, tail

