class Node:
    def __init__(self,val):
        self.val =val
        self.next = None
        self.random = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,val):
        node = Node(val)
        node.next = self.head
        self.head = node
    
    def insert(self,val):
        if not self.head:
            self.head = Node(val)
            return 
        temp = self.head
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

    def clone_random_linked_list(self):
        temp = self.head
        hash = {}
        
        clone = LinkedList()     
        clone.head = Node(temp.val)
        temp2 = clone.head
        hash[id(temp)] = temp2
        
        while temp.next:
            temp = temp.next
            node = Node(temp.val)
            temp2.next = node
            temp2 = temp2.next
            hash[id(temp)] = temp2

        temp = self.head
        temp2 = clone.head
        while temp:
            if temp.random is not None:
                temp2.random = hash.get(id(temp.random))
            else:
                temp2.random = None
            temp = temp.next
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
    clone = ll.clone_random_linked_list()
    clone.display()