def find_subarray_simple(array,x):
    for i in range(len(array)-1):
        _sum = array[i]
        for j in range(i+1,len(array)):
            _sum += array[j]
            if _sum == x:
                return array[i:j+1]
    return None

def find_subarray_two_pointers(array,x):
    """
        this might not work with negative numbers
    """
    l=0
    r=0
    while l<len(array):
        _sum = array[l]
        while _sum<=x and r<len(array)-1:
            r+=1
            _sum+=array[r]
            if _sum == x:
                return array[l:r+1]
        else:
            l+=1
            r=l
    return None

def find_subarray_hash(array,x):
    hash_table = dict()
    _sum = 0
    for i,ele in enumerate(array):
        _sum += ele
        if _sum == x:
            return array[0:i+1]     
        index = hash_table.get(_sum-x)
        if index != None:
            return array[index+1:i+1]
        else:
            hash_table[_sum] = i
        # print(hash_table)
    return None

         
if __name__ == "__main__":
    array=[5,4,6,7,9,8,3,1,2]
    print(find_subarray_simple(array,21))
    print(find_subarray_two_pointers(array,21))
    print(find_subarray_hash(array,21))

    print()
    array=[1, 4, 20, 3, 10, 5]
    print(find_subarray_simple(array,33))
    print(find_subarray_two_pointers(array,33))
    print(find_subarray_hash(array,33))
    
    print()
    array=[1, 4, 0, 0, 3, 10, 5]
    print(find_subarray_simple(array,7))
    print(find_subarray_two_pointers(array,7))
    print(find_subarray_hash(array,7))

    print()
    array=[8,5,-2,3,4,-5,7]
    print(find_subarray_simple(array,10))
    print(find_subarray_two_pointers(array,10))
    print(find_subarray_hash(array,10))

    print()
    array=[10, 2, -2, -20, 10]
    print(find_subarray_simple(array,-10))
    print(find_subarray_two_pointers(array,-10))
    print(find_subarray_hash(array,-10))
