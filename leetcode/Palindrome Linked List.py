class Linkedlist:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        # ond list create madona
        patti = []

        # eliment idre pattige add madu
        while head is not None:
            patti.append(head.val)
            print(f"Added  to list: {patti}")
            # munde eliment na head ge assign madu
            head = head.next
        print(f" Final list: {patti}")
        print(f" Reversed list: {patti[::-1]}")

        # palindrome or not
        return patti == patti[::-1]


# [1,2,2,1]
head = Linkedlist(1)
head.next = Linkedlist(2)
head.next.next = Linkedlist(2)
head.next.next.next = Linkedlist(1)

solution = Solution()
print(solution.isPalindrome(head))

head = Linkedlist(2)
head.next = Linkedlist(2)
head.next.next = Linkedlist(2)
head.next.next.next = Linkedlist(1)

solution = Solution()
print(solution.isPalindrome(head))
