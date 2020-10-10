def equilibrium_index ( array ):
    """
        Time Complexity: O(n^2)
    """
    for i in range(len(array)):
        # print(sum(array[:i]),sum(array[i+1:]))
        if sum(array[:i])==sum(array[i+1:]):  # time complexity of sum() : O(n)
            return i
    return None

def equilibrium_index_2 (array):
    """ 
        Time Complexity: O(n)
    """
    _sum = sum(array)
    left_sum = 0
    for i,ele in enumerate(array):
        _sum-=ele
        if left_sum == _sum:
            return i
        left_sum+=ele
               
      
if __name__ == '__main__':
    array= [-7, 1, 5, 2, -4, 3, 0] 
    print(equilibrium_index(array))
    print(equilibrium_index_2(array))
