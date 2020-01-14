# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
    sum = l1.val + l2.val + carry
    carry = sum//10
    head = ListNode(sum%10)
    if l1.next != None or l2.next != None or carry != 0:
        if l1.next == None:
            l1.next = ListNode(0)
        if l2.next == None:
            l2.next = ListNode(0)
        head.next = self.addTwoNumbers(l1.next,l2.next,carry)
    return head