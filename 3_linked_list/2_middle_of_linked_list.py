class Node:
    def __init__(self,val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def print_linked_list(self):
        temp = self.head 
        while temp:
            print(temp.value,end=" ")
            temp= temp.next
        print()
    
    def middle_element_cache(self):
        visited= []
        temp = self.head
        while temp:
            visited+=[temp.value]
            temp=temp.next
        print(visited[len(visited)//2])

    def middle_element(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow= slow.next
            fast=fast.next.next
        print(slow.value)


if __name__ == '__main__':
    ll = LinkedList()
    # ll.push(6)
    ll.push(5)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    ll.print_linked_list()
    ll.middle_element_cache()
    ll.middle_element()