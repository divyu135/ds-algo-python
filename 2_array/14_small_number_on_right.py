def small_number_on_right_simple( array ):
    result_list = []
    for i in range(len(array)):
        count = 0
        for j in range(i+1,len(array)):
            if array[j]<array[i]:
                count+=1
        result_list += [count]
    return result_list

def small_number_on_right_bisect( array ):
    import bisect
    temp = []
    result_list = []
    for ele in array[-1::-1]:
        result_list+=[bisect.bisect(temp,ele)]
        bisect.insort(temp,ele)
    return list(reversed(result_list))

class Node:
    def __init__(self,val): 
        self.val = val 
        self.left = None
        self.right = None 

        self.ele_count = 1
        self.left_count = 0

class Tree:
    def __init__(self,root): 
        self.root = root 
    def insert(self,node): 
        current = self.root 
        count = 0
        while current!=None: 
            previous = current 
            if node.val>current.val: 
                count += (current.ele_count+current.left_count) 
                current=current.right 
            elif node.val<current.val: 
                current.left_count+=1
                current=current.left 
            else: 
                previous=current 
                previous.ele_count+=1
                break
        if previous.val>node.val: 
            previous.left = node 
        elif previous.val<node.val: 
            previous.right = node 
        else: 
            return count+previous.left_count 
        return count
    
def number_on_right_bst( array ):
    n = len(array)
    t = Tree(Node(array[-1])) 
    ans = [0] 
    for i in range(n-2,-1,-1): 
        ans.append(t.insert(Node(array[i]))) 
    return list(reversed(ans))

if __name__ == "__main__":
    array = [12, 10, 5, 4, 2, 20, 6, 1, 0, 2]
    print(small_number_on_right_simple(array))
    print(number_on_right_bst( array ))
    print(small_number_on_right_bisect( array ))
    print()
    array = [12, 1, 2, 3, 0, 11, 4]
    print(small_number_on_right_simple(array))
    print(number_on_right_bst( array ))
    print(small_number_on_right_bisect( array ))
    print()
    array = [5, 4, 3, 2, 1]
    print(small_number_on_right_simple(array))
    print(number_on_right_bst( array ))
    print(small_number_on_right_bisect( array ))
    print()
    array = [1, 2, 3, 4, 5]
    print(small_number_on_right_simple(array))
    print(number_on_right_bst( array ))
    print(small_number_on_right_bisect( array ))
