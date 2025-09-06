


# Progress below
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for v in values:
        current.next = ListNode(v)
        current = current.next
    
    return dummy.next



'''
l1 = ListNode([1, 2, 4])
This simply means that we created one node with values [1, 2, 4] all together.
'''

'''
1 -> 2 -> 4
1 -> 3 -> 4

if curr1.val <= curr2.val:
    original = curr1
    curr1 = curr1.next
else:
    original = curr2
    curr2 = curr2.next

original = 1 (curr1)
curr1 = 2 -> 4
curr2 = 1 -> 3 -> 4

Start:
original = 1

while curr1 or curr2:
    if curr1 and curr2 and curr1 < curr2:
        original.next = curr1
        curr1 = curr1.next
        original = original.next
    elif curr1 and curr2 and curr1 > curr2:
        original.next = curr2
        curr2 = curr2.next
        original = original.next
    elif curr1 and not curr2:
        original.next = curr1
        curr1 = curr1.next
        original = original.next
    else: # not curr1 and curr2
        original.next = curr2
        curr2 = curr2.next
        original = original.next




curr1 and curr2
    - curr1 > curr2 X
    - curr1 < curr2 X
curr1 and not curr2
    - add in curr1 since that's only left
not curr1 and curr2
    - add in curr2 since that's only left

##### CODE ####################################################################################


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        
        if curr1 and curr2:
            if curr1.val <= curr2.val:
                original = curr1
                curr1 = curr1.next
            elif curr1.val > curr2.val:
                original = curr2
                curr2 = curr2.next
        elif curr1 and not curr2:
            original = curr1
            curr1 = curr1.next            
        elif not curr1 and curr2:
            original = curr2
            curr2 = curr2.next
        else:
            return list1
        
        while curr1 or curr2:
            if curr1 and curr2 and curr1.val < curr2.val:
                original.next = curr1
                curr1 = curr1.next
                original = original.next
            elif curr1 and curr2 and curr1.val > curr2.val:
                original.next = curr2
                curr2 = curr2.next
                original = original.next
            elif curr1 and not curr2:
                original.next = curr1
                curr1 = curr1.next
                original = original.next
            else: # not curr1 and curr2
                original.next = curr2
                curr2 = curr2.next
                original = original.next
        return original


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

My Output: [4]
Expected: [1,1,2,3,4,4]

What if we merged?
1 -> 2 -> 4
1 -> 3 -> 4

list1 = 1 -> 2 -> 4
if list1 >= list2:
    list1.next = list2
    list1 = list1.next
    list2 = list2.next

2 -> 4
3 -> 4
list1 = 1 -> 1 -> 2 -> 4 (at 1)
if list1 < list2:
    list1 = list1.next

2 -> 4
3 -> 4
list1 = 1 -> 1 -> 2 -> 4 (at 2)
list1 = 2 < list2 = 3

4
3 -> 4
list1 = 1 -> 1 -> 2 -> 4 (at 4)
list1 = 1 -> 1 -> 2 -> 3 -> 4 (at 4)
list1 = 1 -> 1 -> 2 -> 3 -> 4 -> 4(at 3)

##### CODE ####################################################################################

while list1 or list2:
    head = list1

    if (list1 and list2 and list1 >= list2):
        list1.next = list2
        list1 = list1.next.next
        list2 = list2.next
    elif (list1 and list2 and list1 < list2) or (list1 and not list2):
        list1 = list1.next
    elif not list1 and list2:
        list1.next = list2
        list1 = list1.next
        list2 = list2.next
    return head

1 -> 2 -> 4
1 -> 3 -> 4

2 -> 4
3 -> 4
1 -> 1 -> 2 -> 4 (at 2)

1 -> 1 -> 2 -> 4 (at 2)

How do I interact with two LL's?
^ "The new list should be made by spliicing together the nodes of the first two lists"
 - ^ Cannot create a new LL


Our output is originally empty - ** So we create a dummy node to avoid edge case of initially empty node **
Giving us the below:
dummy -> 1 -> 1 -> 2 -> 4 -> 4

What would we do if:
    1 -> 2 -> 4
    1 -> 3 -> 4 -> 5 -> 6
Answer: Just take the remainder and place it at the end of our result
'''

