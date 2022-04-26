#Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if not root:
            return []

        if root.left:
            ans += self.inorderTraversal(root.left)
        ans.append(root.val)
        if root.right:
            ans += self.inorderTraversal(root.right)
        return ans