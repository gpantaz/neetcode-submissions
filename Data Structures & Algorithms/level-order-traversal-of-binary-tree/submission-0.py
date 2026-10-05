# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        
        queue = [[root]]
        while queue:
            nodes_at_level = queue.pop(0)
            children = []
            vals = []
            for node in nodes_at_level:
                if node.left:
                    children.append(node.left)
                
                if node.right:
                    children.append(node.right)
                
                vals.append(node.val)
            
            if children:
                queue.append(children)
            res.append(vals)
        
        return res