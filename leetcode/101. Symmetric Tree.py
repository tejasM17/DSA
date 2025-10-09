class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        if not root:  # empty idre true
            return True

        def is_mirror(left, right):

            if not left and not right:  # yavu eliment illandre true
                return True

            if not left or not right:  # only one eliment idre false
                return False

            #  eradu eliment iddu... same eliment agillandre false
            if left.val != right.val:
                return False

            left_ans = is_mirror(left.left, right.right)
            right_ans = is_mirror(left.right, right.left)
            return left_ans and right_ans

        # sub trees elimets same illandre false
        result = is_mirror(root.left, root.right)
        return result


# Create tree nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)
sol = Solution()
print(sol.isSymmetric(root))
