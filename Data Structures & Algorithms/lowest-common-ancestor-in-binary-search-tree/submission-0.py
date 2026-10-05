# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node, target_node):
            queue = [(node, [node])]
            while queue:
                (current_node, current_path) = queue.pop(-1)
                if current_node == target_node:
                    return current_path

                if current_node.left:
                    queue.append((current_node.left, current_path + [current_node.left]))
                    

                if current_node.right:
                    queue.append((current_node.right, current_path + [current_node.right]))

            return None
        
        head = TreeNode(val=-1, left=root)

        path_to_p = dfs(root, p)
        path_to_q = dfs(root, q)

        lca = None
        for node_p, node_q in zip(path_to_p, path_to_q):
            if node_p is node_q:
                lca = node_p
            else:
                break

        return lca

