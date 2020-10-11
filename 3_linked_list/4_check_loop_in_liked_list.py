class Node:
    def __init__(self,val):
        self.value = val
        self.next = None
        self.visited = False

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def travel_approach1(self):
        """
            This will only work if loop is pointing to first element
        """
        temp = self.head
        temp_adr = id(self.head)
        while temp:
            print(temp.value)
            temp=temp.next
            if id(temp) == temp_adr:
                print("There is a loop in the linked list")
                break
    
    def travel_approach2(self):
        """
            using hashmap for storing address/id of each node
        """
        ss = set()
        temp = self.head
        while temp:
            if temp in ss:
                print("There is a loop in linked list")
                break
            
            print(temp.value)
            ss.add(temp)
            temp = temp.next
    
    def travel_approach3(self):
        '''
            this requires modifying the linked list with extra 
            variable visited, if linked list is already provided then
            we need to copy each node to modified node therefore this 
            will require extra space O(n)
        '''
        temp = self.head
        while temp:
            if temp.visited:
                print("There is a loop in the Linked List")
                break
            else:
                print(temp.value)
                temp.visited = True
                temp = temp.next

    def travel_approach4(self):
        '''
            floyds cycle finding algorithm
        '''
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            print(slow.value)
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("There is a loop in the linked list")
                break


if __name__ == "__main__":
    llist = LinkedList() 
    llist.push(20) 
    llist.push(4) 
    llist.push(15) 
    llist.push(10) 
    
    llist.head.next.next.next.next = llist.head.next; 
    
    # llist.travel_approach1() 
    llist.travel_approach2()
    llist.travel_approach3()
    llist.travel_approach4()