def separate_0_1_counting( array ):
    """ 
        Time Complexity: O(n) 
        Space Complexity: O(1)
    """
    count0 = 0
    for ele in array:
        if ele == 0:
            count0+=1
    array[:count0] = [0]*count0
    array[count0:] = [1]*(len(array)-count0)
    return array

def separate_0_1_two_pointer(array):
    """ 
        Time Complexity: O(n) 
        Space Complexity: O(1)
    """
    length=len(array)
    l = 0
    r = length-1
    while l<r:
        while array[l]==0 and l < r:
            l+=1
        while array[r]==1 and l < r:
            r-=1
        if l<r:
            array[l],array[r] = array[r],array[l]
            l+=1
            r-=1
    return array


if __name__ == '__main__':
    array = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
    print(array)
    print(separate_0_1_counting(array))
    print(separate_0_1_two_pointer(array))
    print()
    array = [ 0, 1, 0, 1, 1, 1 ]
    print(array)
    print(separate_0_1_counting(array))
    print(separate_0_1_two_pointer(array))

    