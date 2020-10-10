def separate_even_odd_two_pointer(array):
    """ 
        Time Complexity: O(n) 
        Space Complexity: O(1)
    """
    length=len(array)
    l = 0
    r = length-1
    while l<r:
        while array[l]%2==0 and l < r:
            l+=1
        while array[r]%2==1 and l < r:
            r-=1
        if l<r:
            array[l],array[r] = array[r],array[l]
            l+=1
            r-=1
    return array


if __name__ == '__main__':
    array= [2,7,2,9,4,9,0,8,5,4,4]
    print(array)
    print(separate_even_odd_two_pointer(array))
    print()
    array = [12, 34, 45, 9, 8, 90, 3]
    print(array)
    print(separate_even_odd_two_pointer(array))
