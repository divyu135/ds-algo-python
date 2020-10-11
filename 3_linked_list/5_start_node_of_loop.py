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
    
    def start_of_loop(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if slow != fast :
            print("There is no loop in the Linked List")
            return

        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        print("The loop exist at: ",slow.val)

if __name__ == "__main__":
    l_list = LinkedList() 
    l_list.push(20) 
    l_list.push(4) 
    l_list.push(15) 
    l_list.push(10)
    l_list.push(40) 
    
    l_list.head.next.next.next.next.next = l_list.head.next.next

    l_list.start_of_loop()

    ll = LinkedList() 
    ll.push(20) 
    ll.push(4) 
    ll.push(15) 
    ll.push(10)
    ll.push(40) 
    
    ll.start_of_loop()

    ll.head.next.next.next.next.next = ll.head.next
    ll.start_of_loop()