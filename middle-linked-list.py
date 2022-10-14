class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        node = head
        sumNode = 0

        while node != None:  # percorre a linked list
            sumNode += 1  # soma a quantidade de itens
            node = node.next  # vai para o próximo item

        # cria uma lista que contenha a metade da qnt de itens da linked list
        for i in range(sumNode//2):
            head = head.next  # percorre a lista atribuindo o início da lista para o próximo elemento até chegar na metade

        return head
