from typing import List, Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_binary_tree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        current_node = queue.popleft()

        if arr[i] is not None:
            current_node.left = TreeNode(arr[i])
            queue.append(current_node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            current_node.right = TreeNode(arr[i])
            queue.append(current_node.right)
        i += 1

    return root

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        max_depth = 0

        while queue:
            current_node, depth = queue.popleft()
            max_depth = max(max_depth, depth)

            if current_node.left:
                queue.append((current_node.left, depth + 1))

            if current_node.right:
                queue.append((current_node.right, depth + 1))

        return max_depth

if __name__ == "__main__":
    # Input array
    arr = [3, 9, 20, None, None, 15, 7]

    # Convert list to binary tree
    root = list_to_binary_tree(arr)

    # Find maximum depth
    sol = Solution()
    result = sol.maxDepth(root)
    print(f"Maximum depth of the binary tree is: {result}")
