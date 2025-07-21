# merge_two_lists.py
# Definition for a singly‑linked list node.
class ListNode(object):
    def __init__(self, val=0, next=None):
        # val: holds the integer value of this node
        self.val = val
        # next: points to the next ListNode in the list (or None)
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        Merge two sorted singly‑linked lists list1 and list2
        into a single sorted list, and return its head.

        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # ─── 1. Create a dummy head to simplify edge cases ─────────────────
        head = ListNode()  # dummy node; head.next will be real start
        current = head  # current will "trail" and build the merged list

        # ─── 2. While both lists have nodes, pick the smaller and attach ──
        while list1 and list2:
            if list1.val < list2.val:
                # attach list1’s current node next
                current.next = list1
                # move list1’s pointer forward
                list1 = list1.next
            else:
                # attach list2’s current node next
                current.next = list2
                # move list2’s pointer forward
                list2 = list2.next
            # advance the builder pointer
            current = current.next

        # ─── 3. One list is exhausted; attach the remainder ───────────────
        # (the remaining list is already sorted)
        current.next = list1 or list2

        # ─── 4. Return the real head (skip the dummy) ─────────────────────
        return head.next


# ────────────────────────────────────────────────────────────────────────────────


def build_linked_list(values):
    """
    Helper to turn a Python list into a linked list.
    e.g. [1, 3, 5] → ListNode(1) → ListNode(3) → ListNode(5)
    """
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def print_linked_list(node):
    """
    Helper to print a linked list in easy‑to‑read form.
    e.g. 1 -> 2 -> 4
    """
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print(" -> ".join(vals))


if __name__ == "__main__":
    # Example usage:
    # 1. Build two sample sorted lists
    l1 = build_linked_list([1, 3, 5])
    l2 = build_linked_list([2, 4, 6])

    # 2. Merge them
    sol = Solution()
    merged = sol.mergeTwoLists(l1, l2)

    # 3. Print the result
    print("Merged List:")
    print_linked_list(merged)
