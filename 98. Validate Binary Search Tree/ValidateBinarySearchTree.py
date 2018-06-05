# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(node, lower, upper):
        	if not node:
        		return True
        	if lower is not None and node.val <= lower:
        		return False
        	if upper is not None and node.val >= upper:
        		return False
        	return valid(node.left, lower, node.val) and valid(node.right, node.val, upper)
        return valid(root, None, None)