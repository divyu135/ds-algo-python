def max_element_in_each_window_simple(array,k):
    lst = []
    for i in range(len(array)-k+1):
        _max = array[i]
        for j in range(k):
            if array[i+j]  > _max:
                _max = array[i+j]
        lst.append(_max)
    return lst

def max_element_in_each_window_bst(arrray, k):
    import bisect
    bst = []
    lst =[]
    for i in range(k):
        bisect.insort(bst,array[i])

    for i in range(len(array)-k):
        lst.append(bst[k-1])
        bst.remove(array[i])
        bisect.insort(bst,array[i+k])
    lst.append(bst[k-1])
    return lst

def max_element_in_each_window_deque(array,k):
    from collections import deque 
    li = []
    Qi = deque()
    for i in range(k):
        while Qi and array[i]>=array[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    for i in range(k,len(array)):
        li.append(array[Qi[0]])
        while Qi and Qi[0] <= i-k:
            Qi.popleft()
        while Qi and array[i] >= array[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    li.append(array[Qi[0]])     #print maximum element of last window    
    return li
        
if __name__ == "__main__":
    array = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    print(max_element_in_each_window_simple(array,3))
    print(max_element_in_each_window_bst(array,3))
    print(max_element_in_each_window_deque(array,3))
    print()
    array  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    print(max_element_in_each_window_simple(array,3))
    print(max_element_in_each_window_bst(array,3))
    print(max_element_in_each_window_deque(array,3))
    print()
    array = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    print(max_element_in_each_window_simple(array,4))
    print(max_element_in_each_window_bst(array,4))
    print(max_element_in_each_window_deque(array,4))
