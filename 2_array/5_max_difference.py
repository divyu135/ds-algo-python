def max_difference_simple( array ):
    """
        Time Complexity : O(n)
        Space Complexity : O(1)
    """
    max_difference = array[1]-array[0]
    for i in range(len(array)):
        for ele in array[i+1:]:
            if ele-array[i] > max_difference:
                max_difference = ele-array[i]
    return max_difference

def max_difference_sum_subarray( array ):
    """  
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    difference_array = list()
    for i in range(len(array)-1):
        difference_array.append(array[i+1]-array[i])

    current_differnce = difference_array[0]
    for i in range(1,len(difference_array)):
        if difference_array[i-1] > 0:
            difference_array[i] = difference_array[i-1] + difference_array[i]
        current_differnce = max(current_differnce,difference_array[i])
    return current_differnce

def max_difference_sum_subarray_improved( array ):
    """  
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    diff = array[1]-array[0]

    current_differnce = diff
    for i in range(1,len(array)-1):
        temp_diff = array[i+1]-array[i] 
        if diff > 0:
            temp_diff = diff + temp_diff
        current_differnce = max(current_differnce,temp_diff)
        diff = temp_diff
    return current_differnce

def max_difference_two_pointer( array ):
    """ 
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    _min = array[0] 
    max_difference = None
    for ele in array[1:]:
        if ele < _min : 
            _min =  ele 
        if ele > _min:
            diff = ele - _min
            if max_difference is None or max_difference < diff:
                max_difference = diff
    return max_difference



if __name__ == '__main__':
    array = [2,3,10,6,4,8,1]
    print(max_difference_simple(array))
    print(max_difference_sum_subarray( array ))
    print(max_difference_sum_subarray_improved( array ))
    print(max_difference_two_pointer( array ))
    print()
    array = [7,9,5,6,3,2]
    print(max_difference_simple(array))
    print(max_difference_sum_subarray( array ))
    print(max_difference_sum_subarray_improved( array ))
    print(max_difference_two_pointer( array ))
    print()
    array = [1,2,90,10,110]
    print(max_difference_simple(array))
    print(max_difference_sum_subarray( array ))
    print(max_difference_sum_subarray_improved( array ))
    print(max_difference_two_pointer( array ))