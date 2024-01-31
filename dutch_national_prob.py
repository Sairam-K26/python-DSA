class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    def add_at_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
    def delete_first(self):
        if self.head is None:
            return
        temp=self.head
        self.head = self.head.next
        temp.next=None
    def __str__(self):
        print()
        temp = self.head
        li = []
        while temp:
            li.append('[{0}] -> '.format(temp.data))
            temp = temp.next
        return "".join(li)
    def poland(self): #with swap of data
        curr =self.head
        white=self.head
        while curr:
            if curr.data==0:
                curr.data,white.data=white.data,curr.data
                white=white.next
            curr=curr.next
    def polandd(self): #without swap of data
        f0=None
        f1=None
        l0=None
        l1=None
        th0=None
        th1=None
        temp=self.head
        while temp:
            if temp.data==0:
                if f0==None:
                    f0=temp
                    l0=temp
                    th0=temp
                else:
                    f0=temp
                    l0.next=f0
                    l0=f0
            if temp.data==1:
                if f1==None:
                    f1=temp
                    l1=temp
                    th1=temp
                else:
                    f1=temp
                    l1.next=f1
                    l1=f1
            temp=temp.next
        self.head =th0
        l0.next = th1
        l1.next = None
    def india(self): #without swap of data
        f0=None
        f1=None
        f2=None
        l0=None
        l1=None
        l2=None
        th0=None
        th1=None
        th2=None
        temp=self.head
        while temp:
            if temp.data=='saffron':
                if f0==None:
                    f0=temp
                    l0=temp
                    th0=temp
                else:
                    f0=temp
                    l0.next=f0
                    l0=f0
            if temp.data=='white':
                if f1==None:
                    f1=temp
                    l1=temp
                    th1=temp
                else:
                    f1=temp
                    l1.next=f1
                    l1=f1
            if temp.data=='green':
                if f2==None:
                    f2=temp
                    l2=temp
                    th2=temp
                else:
                    f2=temp
                    l2.next=f2
                    l2=f2        
            temp=temp.next
        self.head =th0
        l0.next = th1
        l1.next = th2
        l2.next = None
li = SingleLinkedList()
li.add_at_last('saffron')
li.add_at_last('white')
li.add_at_last('green')
li.add_at_last('saffron')
li.add_at_last('white')
li.add_at_last('green')
li.add_at_last('saffron')
li.add_at_last('white')
li.add_at_last('green')
li.add_at_last('saffron')
li.add_at_last('white')
li.add_at_last('green')

print(li)
li.india()
print(li)
