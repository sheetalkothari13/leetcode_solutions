class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head
        i = 0
        while temp:
            if i == index:
                return temp.val
            temp = temp.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head
        self.head = new

    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        temp = self.head
        i = 0
        while temp and i < index - 1:
            temp = temp.next
            i += 1

        if temp is None:
            return

        new = ListNode(val)
        new.next = temp.next
        temp.next = new

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        i = 0
        while temp.next and i < index - 1:
            temp = temp.next
            i += 1

        if temp.next:
            temp.next = temp.next.next