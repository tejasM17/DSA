class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # skip duplicates
            else:
                current = current.next

        return head


# Helper: build linked list from Python list
def linked_list(val):
    if not val:
        return None
    head = ListNode(val[0])
    curr = head
    for v in val[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


# Helper: convert linked list to Python list for printing
def lind_ls_to_ls(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


tale = linked_list([1, 1, 2, 3, 3, 3, 4, 5, 5, 6])
utra = Solution()
utra.deleteDuplicates(tale)

print(lind_ls_to_ls(tale))
