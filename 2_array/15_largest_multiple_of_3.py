def largest_multiple_of_3(array):
    _sum = 0
    remainder_0 = []
    remainder_1 = []
    remainder_2 = []
    array = sorted(array,reverse=True)
    for ele in array:
        _sum += ele
        if ele % 3 == 0:
            remainder_0+=[ele]
        elif ele%3==1:
            remainder_1+=[ele]
        else:
            remainder_2+=[ele]
    
    if _sum%3==0:
        return array
    elif _sum%3==1:
        if remainder_1:
            remainder_1.pop()
        elif remainder_2:
            remainder_2.pop()
            remainder_2.pop()
        else:
            return None
    else:
        if remainder_2:
            remainder_2.pop()
        elif remainder_1:
            remainder_1.pop()
            remainder_1.pop()
        else:
            return None

    return sorted(remainder_0+remainder_1+remainder_2, reverse=True)

if __name__ == '__main__':
    array = [1,2,3,4]
    print(largest_multiple_of_3(array))
    print()
    array = [ 8, 1, 7, 6, 0]
    print(largest_multiple_of_3(array))