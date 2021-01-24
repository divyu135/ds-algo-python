class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

# Reverse and clone
def isPalindrome(head):
    if not head:
        return True
    
    length = 0
    temp = head
    head2 = None
    
    while temp:
        node = Node(temp.val)
        node.next = head2
        head2 = node
        length +=1
        temp = temp.next
    
    temp= head
    temp2= head2
    i=0
    while i < length/2:
        if temp.val != temp2.val:
            return False
        temp= temp.next
        temp2=temp2.next
        i+=1
    return True

# Reverse half of the linkedlist
def isPalindrome2(head):

    slow = head
    fast = head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    mid = slow
    
    prev = None
    curr = mid
    while curr:
        temp = curr.next
        curr.next = prev
        prev =curr
        curr = temp
    mid = prev

    temp = head 
    temp2 = mid
    while temp2:
        if temp.val != temp2.val:
            return False
        temp=temp.next
        temp2=temp2.next
    return True



if __name__ == '__main__':

    lst = [1,2,2,1]
    head = Node(lst[0])
    temp = head
    for ele in lst[1:]:
        temp.next = Node(ele)
        temp = temp.next
    print(isPalindrome(head))

    print(isPalindrome2(head))