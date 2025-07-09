# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        def gcd(a , b):
            while b > 0:
                a , b = b , a % b
            return a

        cur = head

        while cur.next:
            n1 , n2 = cur.val , cur.next.val
            cur.next = ListNode(gcd(n1 , n2), cur.next)
            cur = cur.next.next
        return head
    
lis = ListNode(8)
lis.next = ListNode(4)



print(Solution().insertGreatestCommonDivisors(lis))


    # explaination of the code

    # 1. we have a function gcd(a , b) that returns the greatest common divisor of a and b.

    # 2. we have a pointer cur that points to the head of the linked list.

    # 3. we have a while loop that runs until cur.next is None.

    # 4. we have a variable n1 that is equal to cur.val and a variable n2 that is equal to cur.next.val.

    # 5. we have a variable next that is equal to cur.next.next.

    # 6. we have a variable gcd that is equal to the gcd of n1 and n2.

    # 7. we have a variable cur that is equal to cur.next.next.

    # 8. we have a return statement that returns the head of the linked list.
