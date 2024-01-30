class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def add_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_at_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def add_at_index(self, data, index):
        if index <= 0:
            self.add_at_front(data)
            return

        new_node = Node(data)
        temp = self.head
        idx = 0
        while temp is not None and idx != index - 1:
            temp = temp.next
            idx += 1
        if temp is None:
            # reached end of the list
            self.add_at_last(data)
            return
        new_node.next = temp.next
        temp.next = new_node

    def find_element(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    def delete_first(self):
        if self.head is None:
            return
        temp=self.head
        self.head = self.head.next
        temp.next=None
    def delete_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        # temp=self.head
        # if temp.next==None:
        #     self.head=None
        #     return
        # while temp.next.next !=None:
        #     temp=temp.next
        # temp.next=None
    def delete_at_index(self, index):
        if index <= 0:
            self.delete_first()
            return
        temp = self.head
        idx = 0
        while temp and idx != index - 1:
            temp = temp.next
            idx += 1
        if temp is None or temp.next is None:
            # reached end of the list
            return
        temp.next = temp.next.next
    def middleNode(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    # def sorting_linked_list(self):
        



    def __str__(self):
        print()
        temp = self.head
        li = []
        while temp:
            li.append('[{0}] -> '.format(temp.data))
            temp = temp.next
        return "".join(li)

li = SingleLinkedList()
li.add_at_last(30)
li.add_at_last(40)
# print(li)
li.add_at_front(20)
li.add_at_front(10)
print(li)
# li.add_at_index(400, 10)
# print(li)
# print(li.find_element(400))
# li.delete_first()
# print(li)
# li.delete_last()
# print(li)
# li.delete_at_index(1)
# print(li)
midle=li.middleNode()
print(midle)
