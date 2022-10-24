class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sumList = 0

        while l1 != None:
            sumList += l1.val
            l1 = l1.next

        previous = None
        current = self.head

        while(current is not None):
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous

        # TENTAR ENTENDER:

        head = l1
        head2 = l2
        # sum up and find which list is longer
        while l1 and l2:
            SUM = l1.val + l2.val
            l1.val, l2.val = SUM, SUM
            if not l1.next and l2.next:
                head = head2
            l1 = l1.next
            l2 = l2.next
        self.update(head)
        return head

        def update(self, node):
            """deal with the carrying"""
            carry = 0
            while node:
                node.val = node.val + carry
                if node.val >= 10:
                    carry = 1
                    node.val -= 10
                else:
                    carry = 0
                if carry and node.next == None:
                    node.next = ListNode(1)
                    break
                node = node.next
