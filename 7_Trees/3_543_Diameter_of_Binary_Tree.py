# https://leetcode.com/problems/diameter-of-binary-tree/

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

class Solution(object):
    
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.depth(root)
        return self.diameter
    
    def depth(self, node):
        if not node:
            return 0
        
        left_depth=self.depth(node.left)
        right_depth=self.depth(node.right)

        self.diameter = max(self.diameter, left_depth +right_depth)

        return max(left_depth, right_depth) + 1


tree = convertListToTree([1,2,3,4,5])
s = Solution()
print(s.diameterOfBinaryTree(tree))

assert s.diameterOfBinaryTree(tree) == 3

