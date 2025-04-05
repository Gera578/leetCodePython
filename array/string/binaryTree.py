class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:     
    def goodNodes(self,root: Node) -> int:
    #preorder dfs: root, left, right 
        def pre_order_dfs(node, max_value):
            if node is None:
                return 0
            
            if node.val >= max_value:
                good = 1
            else:
                good = 0
            
            #update maximum value seen so far, to keep track
            max_value = max(max_value, node.val)
            
            good += pre_order_dfs(node.left, max_value)
            good += pre_order_dfs(node.right, max_value)
            
            return good
    
        return pre_order_dfs(root, root.val)
        
        
    
    

root = Node(3) 
root.left = Node(1) 
root.right = Node(4)
root.left.left = Node(3)
root.right.left = Node(1)
root.right.right = Node(5)
solution = Solution()
print(solution.goodNodes(root))
