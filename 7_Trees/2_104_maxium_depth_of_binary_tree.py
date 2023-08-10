# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertListToTree(lst):
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1

    while i < len(lst):
        node = queue.pop(0)

        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)

        i += 1

        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)

        i += 1

    return root

def convertTreeToList(root):
    if not root:
        return []

    queue = [root]
    lst = []

    while queue:
        node = queue.pop(0)
        lst.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return lst

class Solution(object):
    def __init__(self):
        self.depth = 0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
    
tree =  convertListToTree([3,9,20,None,None,15,7])
s = Solution()
print(s.maxDepth(tree))
assert s.maxDepth(tree) == 3
