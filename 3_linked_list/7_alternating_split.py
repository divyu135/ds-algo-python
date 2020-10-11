class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def display(self):
        temp = self.head
        while temp:
            print("val= ",temp.val,"id= ", id(temp),end=' ')
            temp = temp.next
        print()

def alternating_lists(ll):
    temp = ll.head
    ll2 = LinkedList()
    ll2.head = ll.head.next
    
    while temp.next:
        t = temp.next
        temp.next = temp.next.next
        temp = t
    
    ll.display()
    ll2.display()
if __name__ == '__main__':
    ll = LinkedList()
    ll.push(6)
    ll.push(5)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    ll.push(11)

    ll.display()
    alternating_lists(ll)
    