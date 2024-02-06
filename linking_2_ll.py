class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

def length(head):
    count = 0
    temp = head
    while temp:
        temp = temp.next
        count += 1
    return count

def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    len1 = length(head1)
    len2 = length(head2)
    
    if len1 <= len2:
        temp = head1
        temp.next = merge(head1.next, head2)
    else:
        temp = head2
        temp.next = merge(head1, head2.next)
    return temp

def find_if_merged_linked_list(head):
    if not head:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)
head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
display(merge(head1, head2))
print(length(head1))
display(find_if_merged_linked_list(head1))