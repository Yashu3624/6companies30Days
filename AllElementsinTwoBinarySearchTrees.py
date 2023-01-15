# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        def preorder(node:TreeNode) -> None:
            if not node:
                return None
            ans.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root1)
        preorder(root2)
        return sorted(ans)