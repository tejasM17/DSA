class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        # edge case na handel madoke
        if not p and not q:
            return True
        if not p or not q:
            return False
        # wrong jodi idre False
        if p.val != q.val:
            print(f" differ {p.val} != {q.val}")
            return False
        # kelage iro node galanna na check madbeku
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right
