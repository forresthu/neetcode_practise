
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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.isBalancedTree = True
        self.breakProcess = False 

        self.checkBalance(root)

        return self.isBalancedTree
    
    def checkBalance(self, root):
        if not root or self.breakProcess:
            return 0
        
        left_depth = self.checkBalance(root.left)
        rigth_depth = self.checkBalance(root.right)
        print(tree.val, left_depth, rigth_depth)
        if abs(left_depth - rigth_depth) >1 :
            self.isBalancedTree = False
            self.breakProcess = True

        return max(left_depth, rigth_depth) +1
    
s=Solution()
tree = convertListToTree([3,9,20,None,None ,15,7])
assert s.isBalanced(tree) == True

tree = convertListToTree([1,2,2,3,3,None,None,4,4])
assert s.isBalanced(tree) == False
