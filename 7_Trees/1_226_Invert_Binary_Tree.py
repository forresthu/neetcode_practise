# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
## Create two utility functions. One is to convert List to Tree, the other is to convert Tree to List. The key point of design is to have a queue to hold node in pipeline for processing.

## Benefit of practising Leetcode is distill programming technicals, such using queue, stack, and recursive etc in real project. 

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
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

tree =  convertListToTree([4,2,7,1,3,6,9])
s = Solution()

invertedTree = s.invertTree(tree)
print(convertTreeToList(invertedTree))

