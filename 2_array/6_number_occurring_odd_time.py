def number_occurring_odd_times_simple( array ):
    """ 
        Time Complexity : O(n^2)
        Space Complexity: O(1)
    """
    for element in array:
        count=0
        for ele in array:
            if ele == element:
                count+=1
        if count%2==1:
            return element
    return None

def number_occurring_odd_times_hashtable( array ):
    """ 
        Time Complexity: O(n)
        Space Complexity: O(n) 
    """
    hashtable = dict()
    for ele in array:
        if hashtable.get(ele):
            hashtable[ele]+=1
        else:
            hashtable[ele]=1
    for key in hashtable.keys():
        if hashtable[key]%2==1:
            return key
    return None

def number_occurring_odd_times_xor( array ):
    """ 
        Time Complexity: O(n) 
        Space Complexity: O(1)
    """
    odd_number=0
    for ele in array:
        odd_number ^= ele
    return odd_number

if __name__ == '__main__':
    array = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2 ]
    print( number_occurring_odd_times_simple(array))
    print(number_occurring_odd_times_hashtable( array ))
    print(number_occurring_odd_times_xor( array ))
    print()
    array = [1, 2, 3, 2, 3, 1, 3]
    print( number_occurring_odd_times_simple(array))
    print(number_occurring_odd_times_hashtable( array ))
    print(number_occurring_odd_times_xor( array ))
    print()
    array = [5, 7, 2, 7, 5, 2, 5]
    print( number_occurring_odd_times_simple(array))
    print(number_occurring_odd_times_hashtable( array ))
    print(number_occurring_odd_times_xor( array ))
