class Solution(object):
    def isPalindrome(self, head):
        lista = []
        current = head

        while current:
            lista.append(current.val)
            current = current.next

        return lista == lista[::-1]
