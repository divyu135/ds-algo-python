class Node:
    def __init__(self,val):
        self.val = val;
        self.next = None;

def mergeTwoLinkeList(head1, head2):
    
    if head1.val < head2.val:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next
    
    temp = head
    while head1 and head2:
        if head1.val < head2.val:
            head.next = head1
            head1 = head1.next
        else:
            head.next = head2
            head2 = head2.next
        head = head.next
   
    if (head1):
        head.next = head1
    else:
        head.next = head2
    return temp

if __name__ == '__main__': 
  
    head1 = Node(10)
    temp = head1
    for i in [20,30,40,50,90,100,122]:
        temp.next = Node(i)
        temp = temp.next 

  
    head2 = Node(5)
    temp = head2
    for i in [15,19,35,60]:
        temp.next = Node(i)
        temp = temp.next  
    
    head = mergeTwoLinkeList(head1,head2)
    temp = head
    while temp:
        print(temp.val,end=' ')
        temp = temp.next
    print()
    

