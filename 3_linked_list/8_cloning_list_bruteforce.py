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
    
    def insert(self,val):
        temp = self.head
        while temp.next:
            temp = temp.next
        node = Node(val)
        temp.next = node
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.val," next ", id(temp.next)," random ",id(temp.random),end='\n')
            temp = temp.next
        print()

    def clone_random_linked_list(self):
        temp = self.head
        clone_lst = LinkedList()
        t = clone_lst.head = Node(temp.val)
        while temp.next:
            temp = temp.next
            t.next = Node(temp.val)
            t= t.next
        
        temp = self.head
        t= clone_lst.head

        while temp:
            rv = temp.random.val
            t2 = clone_lst.head
            while(t2.val!=rv):
                t2 = t2.next
            t.random = t2
            t = t.next
            temp =temp.next

        return clone_lst

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
