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
            print(temp.val, end=" ")
            temp = temp.next
    
def merging_point_approach1(list1,list2):
    temp1 = list1.head
    while temp1:
        temp2 = list2.head
        while temp2:
            if temp1 is temp2:
                return temp1.val
            temp2 = temp2.next
        temp1 = temp1.next
    return None

def merging_point_approach2(list1,list2):
    s = set()
    temp = list1.head
    while temp:
        s.add(temp)
        temp = temp.next
    temp = list2.head
    while temp:
        if temp in s:
            return temp.val
        temp = temp.next
    return None

def merging_point_approach3(list1,list2):
    stack1 = list()
    stack2 = list()
    temp = list1.head
    while temp:
        stack1+=[temp]
        temp = temp.next
    temp = list2.head
    while temp:
        stack2+=[temp]
        temp = temp.next
    merge = None
    while stack1 and stack2:
        a = stack1.pop()

        b = stack2.pop()

        if a is b :
            merge = a.val
        else:
            break
    return merge
        
def merging_point_approach4(list1,list2):
    def length(ll):
        l=0
        temp = ll.head
        while temp:
            l+=1
            temp =temp.next
        return l

    l1 = length(list1)
    l2 = length(list2)
    if l1>=l2:
        l = l1-l2
        first = list1.head
        second = list2.head
    else:
        l = l2-l1
        first = list2.head
        second = list1.head
    
    while l>0:
        first =first.next
        l-=1
    
    while first and second:
        if first is second :
            return first.val
        first = first.next
        second = second.next
    return None

def merging_point_approach5(list1,list2):
    def start_of_loop(ll):
        slow = ll.head
        fast = ll.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if slow != fast :
            return None

        slow = ll.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow.val
    
    t = list1.head
    while t.next:
        t = t.next
    t.next = list1.head
     
    merge = start_of_loop(list2)
    t = None
    return merge

if __name__ == "__main__":
    list1 = LinkedList()
    list1.push(2)
    list1.push(3)
    list1.push(4)
    list1.push(5)
    list1.push(6)
    list1.push(8)
    list1.display()
    print()
    list2 = LinkedList()
    list2.push(20)
    list2.push(30)
    list2.push(40)
    list2.head.next.next.next = list1.head.next.next
    list2.display()
    print()

    print(merging_point_approach1(list1,list2))
    print(merging_point_approach2(list1,list2))
    print(merging_point_approach3(list1,list2))
    print(merging_point_approach4(list1,list2))
    print(merging_point_approach5(list1,list2))