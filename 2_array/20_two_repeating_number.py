def two_repeating_numbers_simple(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] == array[j]:
                print(array[i],end=" ")
                break
    print()

def two_repeating_numbers_sign_change(array):
    for i in range(len(array)):
        if array[abs(array[i])] > 0:
            array[abs(array[i])] *= -1
        else:
            print(abs(array[i]),end= " ")
    print()

def two_repeating_numbers_counting(array):
    counter = {}
    for ele in array:
        if counter.get(ele) == 1:
            print(ele,end=" ")
        else:
            counter[ele] = 1
    print()   

def two_repeating_numbers_maths(array):
    from math import factorial
    from math import sqrt
    
    n = len(array)-2

    sum_num = n*(n+1)//2
    sum_array = 0
    product_num = factorial(n)
    product_array = 1
    
    for ele in array:
        sum_array += ele
        product_array *= ele
    
    x_plus_y = sum_array  - sum_num
    xy = product_array // product_num
    x_minus_y = sqrt(x_plus_y**2 - 4*xy)
    x = int(x_plus_y + x_minus_y)//2
    y = x_plus_y - x

    print(x,y)

def two_repeating_numbers_xor(array):
    n = len(array)-2
    x_xor_y = array[0]
    
    for ele in array[1:]:
        x_xor_y ^= ele

    for ele in range(1,n+1):
        x_xor_y ^= ele
        
    mask = x_xor_y & ~(x_xor_y-1)

    group1 = []
    group2 = []
    group_a = []
    group_b = []
    
    for ele in array:
        if ele & mask :
            group1+=[ele]
        else:
            group2+=[ele]
    for i in range(1,n+1):
        if i & mask:
            group_a += [i]
        else:
            group_b += [i]
    
    x = group1[0]
    for ele in group1[1:]+group_a:
        x ^= ele
    y = group2[0]
    for ele in group2[1:]+group_b:
        y ^= ele
    
    print(x,y)

if __name__ == '__main__':
    array = [1,2,1,4,4,5,3]
    two_repeating_numbers_simple(array)
    two_repeating_numbers_counting(array)
    two_repeating_numbers_maths(array)
    two_repeating_numbers_xor(array)
    two_repeating_numbers_sign_change(array)
    print()
    array = [4, 2, 4, 5, 2, 3, 1]
    two_repeating_numbers_simple(array)
    two_repeating_numbers_counting(array)
    two_repeating_numbers_maths(array)
    two_repeating_numbers_xor(array)
    two_repeating_numbers_sign_change(array)
