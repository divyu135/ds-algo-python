class Node :
    def __init__(self,val):
        self.val = val
        self.nxt = None

class LinkedList():
    def __init__(self):
        self.head = None
    

    def reverse(self):
        current = self.head
        previous = None
        while current:
            next_node = current.nxt
            current.nxt = previous
            previous = current
            current = next_node
        self.head = previous

    def push(self, val):
        node = Node(val)
        node.nxt = self.head
        self.head = node

    def insert(self,val):
        temp = self.head
        while temp.nxt:
            temp = temp.nxt
        node = Node(val)
        temp.nxt = node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.nxt

if __name__ == '__main__':
    ll = LinkedList()
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    ll.insert(5)
    ll.insert(6)
    ll.print_list()
    ll.reverse()
    print()
    ll.print_list()