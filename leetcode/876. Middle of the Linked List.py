class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        count = 0
        temp = head

        while temp:
            count += 1
            temp = temp.next

        for i in range(count // 2):
            head = head.next

        return head
