class Listnode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):
        dummy = Listnode(0)
        temp = dummy
        cur = head  # idu input list

        while cur:

            if cur.val != val:
                temp.next = cur  # next eliment na cur ge serisu
                temp = temp.next  # next eliment na tago
                cur = cur.next
            else:
                cur = cur.next

        # enu ill andre
        temp.next = None

        return dummy.next


def print_list(head):
    current = head
    while current:
        print(current.val, "->", end=" ")
        current = current.next
    print("None")


# Create linked list: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
head = Listnode(1)
head.next = Listnode(2)
head.next.next = Listnode(6)
head.next.next.next = Listnode(3)
head.next.next.next.next = Listnode(4)
head.next.next.next.next.next = Listnode(5)
head.next.next.next.next.next.next = Listnode(6)


print("list : c")
print_list(head)

solution = Solution()
new_head = solution.removeElements(head, 6)

print("6 na tegudmele : ")
print_list(new_head)
