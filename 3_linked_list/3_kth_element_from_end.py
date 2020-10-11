class Node:
    def __init__(self,val):
        self.value = val
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None

    def push(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def kth_element_from_end_approach1(self,k):
        l = 0
        temp = self.head
        while temp:
            temp=temp.next
            l+=1
        i=0
        temp = self.head
        while i<l-k:
            temp=temp.next
            i+=1
        print(temp.value)
    
    def kth_element_from_end_approach2(self,k):
        visited = []
        temp = self.head
        while temp:
            visited+=[temp.value]
            temp = temp.next
        print(visited[-k])        

    def kth_element_from_end_approach3(self,k):
        front = self.head
        back = self.head
        for i in range(k):
            front = front.next
        while front:
            front=front.next
            back=back.next
        print(back.value)

if __name__ == "__main__":
    ll = LinkedList()
    ll.push(5)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    ll.kth_element_from_end_approach1(2)
    ll.kth_element_from_end_approach2(2)
    ll.kth_element_from_end_approach3(2)
