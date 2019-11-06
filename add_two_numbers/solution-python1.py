# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr_digit = 0
        carry = 0

        # create the head of resulting list
        if l1 is not None and l2 is not None:
            new_val = (10 ** curr_digit) * (l1.val + l2.val)

            result = ListNode(new_val % 10)
            carry = new_val // 10
            l1, l2 = l1.next, l2.next
        else:
            return None

        # create new nodes off the current_node
        curr_node = result

        # copy while both lists have digits
        while l1 is not None and l2 is not None:
            new_val = (10 ** curr_digit) * (l1.val + l2.val) + carry

            curr_node.next = ListNode(new_val % 10)
            carry = new_val // 10
            l1, l2, curr_node = l1.next, l2.next, curr_node.next

        # copy the remaining digits from one of the lists (if any)
        list_to_copy = l1 if l1 is not None else l2
        while list_to_copy is not None:
            new_val = (10 ** curr_digit) * list_to_copy.val + carry

            curr_node.next = ListNode(new_val % 10)
            carry = new_val // 10
            list_to_copy, curr_node = list_to_copy.next, curr_node.next

        # check if a new node must be created from carry
        if carry != 0:
            curr_node.next = ListNode(carry)

        return result
