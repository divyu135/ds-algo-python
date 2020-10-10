def pair_sum_closest_to_zero ( array ):
    """
        Time Complexity: O(n*log(n))     time complexity of sorting array
        Space Complexity: O(1)
    """
    l = 0
    r = len(array)-1
    
    array = sorted(array)

    min_l, min_r = l,r
    min_sum = float("inf")
    
    while l<r:
        _sum = array[l]+array[r]
        if _sum == 0:
            return (array[l],array[r])

        if abs(_sum) < abs(min_sum):
            min_sum = _sum
            min_l = l
            min_r = r

        if _sum >0:
            r-=1
        elif _sum < 0:
            l+=1
    return (array[min_l],array[min_r])

if __name__ == '__main__':
    array = [1, 60, -10, 70, -80, 85] 
    print(pair_sum_closest_to_zero(array))