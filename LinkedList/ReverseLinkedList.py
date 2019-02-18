# Problem Statement #206: https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse_list(self, head: 'ListNode') -> 'ListNode':
        new_head = None
        pointer = head

        while pointer is not None:
            temp_node = pointer.next            
            pointer.next = new_head
            new_head = pointer
            pointer = temp_node

        return new_head

    def __eq__(self, subject, other):
        return
        return self.path == other.path and self.title == other.title

    def print_linked_nodes(self, new_head):
        while new_head is not None:
            print(new_head.val)
            new_head = new_head.next


# Test Case

s = Solution()

input = ListNode(1)
input.next = ListNode(2)
input.next.next = ListNode(3)
input.next.next.next = ListNode(4)
input.next.next.next.next = ListNode(5)
input.next.next.next.next.next = None
result = s.reverse_list(input)
s.print_linked_nodes(result)  # should print 5 4 3 2 1

input = ListNode(1)
result = s.reverse_list(input)
s.print_linked_nodes(result)  # should print 1

input = None
result = s.reverse_list(input)
s.print_linked_nodes(result)  # should print (Nothing)
