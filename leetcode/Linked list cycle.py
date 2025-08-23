# 1. Start at head.
# 2. Keep a record of visited nodes (like a set).
# 3. While walking through list:
#      - If current node is already in the set → return True
#      - Otherwise, add node to set
#      - Move to next node
# 4. If we reach None → return False


class ListNode:  # use correct name (capital N is common style)
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):
        visited = set()  # set

        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next

        return False


# Helper function to build linked list
def linked_list(val, pop):
    nodes = [ListNode(v) for v in val]  # [] = list comprehension (indexable ✅)
    # () = generator (not indexable ❌).

    # connect nodes in chain
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # if pos != -1, create cycle to redirect
    if pop != -1:
        nodes[-1].next = nodes[pop]

    return nodes[0]


utra = Solution()
head = linked_list([1, 2, 3, 2, 4], 1)
print(utra.hasCycle(head))

# print(utra.hasCycle([1, 2, 3, 2, 4]))  #  TypeError: unhashable type: 'list'

# is_visted = {1, 2, 3, 2}
# print(type(is_visted), is_visted)
# output : <class 'set'> {1, 2, 3}
