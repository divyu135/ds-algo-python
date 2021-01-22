class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.random = None
    
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
            nxt = temp.next.val if temp.next else None
            rnd = temp.random.val if temp.random else None
            print(temp.val," next ", nxt," random ",rnd,end='\n')
            temp = temp.next
        print()
    
    def clone_linked_list(self):
        
        if not self.head:
            return 
        temp = self.head
        while temp:
            t = temp.next
            node = Node(temp.val)
            temp.next = node
            node.next = t
            temp = t
        
        # Assigning random pointer in new linked list
        temp = self.head
        while temp:
            temp.next.random = temp.random.next
            temp = temp.next.next

        # Splitting the Merged linkedList
        clone = LinkedList()
        temp = self.head
        clone.head = self.head.next
        while temp.next:
            t = temp.next
            temp.next = temp.next.next
            temp = t

        return clone

if __name__ == "__main__":
    ll = LinkedList()
    ll.push(50)
    ll.push(40)
    ll.push(30)
    ll.push(20)
    ll.push(10)
    
    ll.head.random = ll.head.next.next
    ll.head.next.next.random = ll.head.next.next.next.next
    ll.head.next.next.next.next.random = ll.head.next
    ll.head.next.next.next.random = ll.head.next.next
    ll.head.next.random = ll.head

    ll.display()
    clone = ll.clone_linked_list()
    clone.display()