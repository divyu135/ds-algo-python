def find_subarray(array):
    hash_table = dict()
    _sum = 0
    for i,ele in enumerate(array):
        _sum += ele
        if _sum == 0:
            return array[0:i+1]
        ind = hash_table.get(_sum)
        if ind!=None:    
            return array[ind+1:i+1]
        else:
            hash_table[_sum]=i
    return None

if __name__ == "__main__":
    array=[5,4,-3,-2,-4,9,8,3,1,2]
    print(find_subarray(array))