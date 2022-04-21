#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # root를 확인하고, 왼쪽 서브트리와 오른쪽 서브트리를 확인하는 방식으로 해결 !
        # 단, 대칭을 확인하기 위해서는 왼쪽 서브트리와 오른쪽 서브트리를 반대로 비교해야함.
        # 두 서브트리의 root가 같은지 확인하고, 왼쪽 서브트리의 left가 오른쪽 서브트리의 right가 같은지
        # 왼쪽 서브트리의 right이 오른쪽 서브트리의 left가 같은지 확인.
        def traversal(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            else:
                return left.val == right.val and traversal(left.left, right.right) and traversal(left.right, right.left)

        return traversal(root, root)