import heapq
# heapify, heappush, heappop

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def merge_k_sorted_linke_list(lists):
    lst = []
    dic = {}

    for ll in lists:
        heapq.heappush(lst,ll.val)
        if dic.get(ll.val):
            dic[ll.val].append(ll)
        else:
            dic[ll.val] = [ll]
    head= Node(0)
    temp = head
    while lst:
        n_val = heapq.heappop(lst)        
        node = dic[n_val].pop(0)
        temp.next = node
        temp = temp.next
        if node.next:
            heapq.heappush(lst,node.next.val)
            if dic.get(node.next.val):
                dic[node.next.val].append(node.next)
            else:
                dic[node.next.val] = [node.next]
    return head.next

if __name__ == "__main__":
    arr1 = Node(1);
    arr1.next = Node(3);
    arr1.next.next = Node(5);
    arr1.next.next.next = Node(7);
 
    arr2 = Node(2);
    arr2.next = Node(4);
    arr2.next.next = Node(6);
    arr2.next.next.next = Node(8);
 
    arr3 = Node(0);
    arr3.next = Node(9);
    arr3.next.next = Node(10);
    arr3.next.next.next = Node(11);

    head = merge_k_sorted_linke_list([arr1,arr2,arr3])

    temp = head
    while temp:
        print(temp.val,end=' ')
        temp = temp.next
    print()



# Leetcode solution

    # def mergeKLists(self, lists):
    #     """
    #     :type lists: List[ListNode]
    #     :rtype: ListNode
    #     """
    #     head = point = ListNode(0)
    #     q = PriorityQueue()
    #     for l in lists:
    #         if l:
    #             q.put((l.val, l))
    #     while not q.empty():
    #         val, node = q.get()
    #         point.next = ListNode(val)
    #         point = point.next
    #         node = node.next
    #         if node:
    #             q.put((node.val, node))
    #     return head.next