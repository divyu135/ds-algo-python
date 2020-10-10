def triplet_simple ( array, x ):
    """ 
        Time Complexity: O(n^3) 
        Space Complexity: O(1)
    """
    for i in range(len(array)-2):
        for j in range(i+1,len(array)-1):
            for k in range(j+1,len(array)):
                if array[i]+array[j]+array[k] == x:
                    return (array[i],array[j],array[k])
    return None

def binary_search(arr, x,i,j): 
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high: 
        mid = (high + low) // 2
        if arr[mid] < x: 
            low = mid + 1
        elif arr[mid] > x: 
            high = mid - 1
        else:
            if mid != i and mid != j: 
                return mid 
    return None

def triplet_binary_search( array, x):
    """
        Time Complexity : O(n*log(n) + O(n^2 * log(n)) 
                        : O(n^2 * log(n))
    """
    array = sorted(array)
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            target = x - (array[i] + array[j])
            k = binary_search(array,target,i,j)
            if k:
                return (array[i],array[j],array[k])
    return None

def triplet_two_pointers( array, x):
    """
        Time Complexity: O(n^2)
    """
    array = sorted(array)
    for i in range(len(array)-2):
        l = i+1
        r = len(array)-1
        while l<r:
            _sum = array[i]+array[l]+array[r]
            if _sum == x:
                return (array[i],array[l],array[r])
            elif _sum < x:
                l+=1
            else:
                r-=1
    return None

if __name__ == '__main__':
    array = [1, 4, 45, 6, 10, 8] 
    x=22
    print(triplet_simple(array,x))
    print(triplet_binary_search(array, x))
    print(triplet_two_pointers( array, x))