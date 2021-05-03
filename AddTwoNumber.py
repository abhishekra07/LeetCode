""""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

l1 = 2 -> 4 -> 3
l2 = 5 -> 6 -> 4

output = 7 -> 0 -> 8

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = LinkedlistToInt(l1)
        num2 = LinkedlistToInt(l2)
        num3 = num1 + num2
        newnum = str(num3)[::-1]
        res = [int(x) for x in str(newnum)]
        node = None
        for i in res:
            if not node:
                node = ListNode(val=i)
            else:
                temp = node
                while temp.next:
                    temp = temp.next
                temp.next = ListNode(val=i)
        return node
        
def LinkedlistToInt(head):
    number = 0
    position = 0
    while head:
        number = number + head.val * (10 ** position)
        # print("number {0} head.val {1} position {2}".format(number, head.val, position))
        head = head.next
        position += 1
    return number

