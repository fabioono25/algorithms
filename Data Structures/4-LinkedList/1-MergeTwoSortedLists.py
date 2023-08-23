# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Example 1: Input: list1 = [1,2,4], list2 = [1,3,4] Output: [1,1,2,3,4,4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time: O(n+m) | Space: O(1) 
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    lRet = ListNode()

    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    if l1.val <= l2.val:
        lRet = l1
        lRet.next = mergeTwoLists(l1.next, l2)
    else:
        lRet = l2
        lRet.next = mergeTwoLists(l1, l2.next)
    
    return lRet

# without recursion
def mergeTwoLists2(l1: ListNode, l2: ListNode) -> ListNode:
    lRet = ListNode()
    lCurr = lRet

    while l1 and l2:
        if l1.val <= l2.val:
            lCurr.next = l1
            l1 = l1.next
        else:
            lCurr.next = l2
            l2 = l2.next
        lCurr = lCurr.next
    
    if l1:
        lCurr.next = l1
    if l2:
        lCurr.next = l2
    
    return lRet.next

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

answer = mergeTwoLists(l1, l2)

print("Solution 1: ")
while answer:
    print(answer.val)
    answer = answer.next

l3 = ListNode(1, ListNode(2, ListNode(4)))
l4 = ListNode(1, ListNode(3, ListNode(4)))

answer2 = mergeTwoLists2(l3, l4)


print("Solution 2: ")
while answer2:
    print(answer2.val)
    answer2 = answer2.next