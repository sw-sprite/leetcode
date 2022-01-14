from typing import Callable, Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_node_list(values: List[int]) -> ListNode:
    """Creates a ListNode out of a list of values"""
    head = ListNode(values[0])

    last_node = head
    for value in values[1:]:
        node = ListNode(value)
        last_node.next = node
        last_node = node

    return head


def get_values(node: ListNode) -> List[int]:
    """Returns the values in linked list"""
    values = [node.val]
    curr = node.next
    while curr is not None:
        values.append(curr.val)
        curr = curr.next

    return values

class Solution:
    # def addTwoNumbers(
    #     self,
    #     l1: Optional[ListNode], 
    #     l2: Optional[ListNode]
    # ) -> Optional[ListNode]:
    #     head = ListNode(0)
    #     cur_node = head
    #     carry_over = 0
    #     d1 = 0
    #     d2 = 0
    #     while True:
            
    #         if l1 is not None:
    #             d1 = l1.val
    #         else: 
    #             d1 = 0
    #         if l2 is not None:
    #             d2 = l2.val
    #         else: 
    #             d2 = 0
            
    #         cur_d = (d1 + d2 + carry_over) % 10 
    #         carry_over = ((d1 + d2 + carry_over) //10) % 10
            
    #         cur_node.val = cur_d

    #         if l1 is not None:
    #             l1 = l1.next
    #         if l2 is not None:
    #             l2 = l2.next
            
    #         if l1 == None and l2 == None and carry_over == 0:
    #             return head
            
    #         cur_node.next = ListNode(0)
    #         cur_node = cur_node.next

    def addTwoNumbers(
        self,
        l1: Optional[ListNode], 
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # slightly cleaner, not faster
        
        head = ListNode(0)
        cur_node = head
        carry_over = 0
        d1 = 0
        d2 = 0
        while not(l1 == None and l2 == None and carry_over == 0):
            
            if l1 is not None:
                d1 = l1.val
                l1 = l1.next
            else: 
                d1 = 0
            if l2 is not None:
                d2 = l2.val
                l2 = l2.next
            else: 
                d2 = 0
            
            cur_node.next = ListNode((d1 + d2 + carry_over) % 10 )
            cur_node = cur_node.next

            carry_over = (d1 + d2 + carry_over) //10
        

        return head.next        

###########################################################
# testing stuff
###########################################################


tests = [
    (
        ([2, 4, 3], [5, 6, 4],),
        [7, 0, 8],
    ),
    (
        ([0], [0],),
        [0],
    ),
    (
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9],),
        [8, 9, 9, 9, 0, 0, 0, 1],
    ),
]

def validator(
    addTwoNumbers: Callable[[Optional[ListNode], Optional[ListNode]], Optional[ListNode]], 
    inputs,
    expected
) -> None:
    values1, values2 = inputs
    node_list1 = create_node_list(values1) if len(values1) > 0 else None
    node_list2 = create_node_list(values2) if len(values2) > 0 else None
    new_list = addTwoNumbers(node_list1, node_list2)

    list_values = get_values(new_list) if new_list is not None else []
    assert list_values == expected, (list_values, expected)