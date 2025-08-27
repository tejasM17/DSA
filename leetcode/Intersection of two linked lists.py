class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Create intersecting lists (example from problem)
intersect = ListNode(8)  # Shared part starts here
intersect.next = ListNode(4)
intersect.next.next = ListNode(5)

heada = ListNode(4)  # List A: 4 → 1 → 8 → 4 → 5
heada.next = ListNode(1)
heada.next.next = intersect

headb = ListNode(5)  # List B: 5 → 6 → 1 → 8 → 4 → 5
headb.next = ListNode(6)
headb.next.next = ListNode(1)
headb.next.next.next = intersect


class Solution:
    def getIntersectionNode(self, heada, headb):

        if not heada or not headb:
            return None

        pa = heada
        print(f"pa : {pa.val}")
        pb = headb
        print(f"pb : {pb.val}")
        while pa != pb:
            pa = pa.next if pa else headb
            print(f"headA : {heada.val}")
            pb = pb.next if pb else heada
            print(f"headB : {headb.val}")
        return pa


sol = Solution()
intersection = sol.getIntersectionNode(heada, headb)
if intersection:
    print(f"Intersection at node with value: ' {intersection.val} '")
else:
    print("No intersected")
