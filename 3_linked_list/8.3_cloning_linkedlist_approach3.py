class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.random = None

class LinkedList:
    def __init__(self):
        self.head =None
    
    def push(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def append(self, val):
        if not self.head:
            self.head = Node(val)
            return
        temp =self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(val)

    def display(self):
        temp =self.head
        while temp:
            nxt = temp.next.val if temp.next else None
            rnd = temp.random.val if temp.random else None
            print(temp.val," next ", nxt," random ",rnd,end='\n')
            temp = temp.next
        print()
    
    def clone_linked_list(self):
        clone = LinkedList()
        
        temp = self.head
        clone.head = Node(temp.val)
        temp2 = clone.head
        pointer = temp.next
        temp2.random = temp
        temp.next = temp2

        while pointer:
            # print(temp2.random.val)
            temp = pointer
            temp2.next = Node(temp.val)
            temp2 = temp2.next
            
            pointer = temp.next
            temp2.random = temp
            temp.next = temp2
        # print(temp2.random.val)

        temp2 = clone.head
        while temp2:
            temp2.random = temp2.random.random.next
            temp2 = temp2.next     
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
    
    # Original list will be distorted so, not recommended
    # ll.display()