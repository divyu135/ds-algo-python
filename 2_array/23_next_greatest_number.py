def next_greater_number(array):
    i = len(array)-2
    while i>=0:
        if array[i]<array[i+1]:
            break
        i-=1
    else:
        print("Not Possible")
        return
    
    _min,m = float("inf"),None
    for j in range(i+1,len(array)):
        if array[j] > array[i] and array[j] < _min:
            _min = array[j]
            m =j
    array[i],array[m] = array[m],array[i]

    n = (len(array)- (i+1))//2
    for k in range(1,n+1):
        array[i+k],array[-k] = array[-k],array[i+k]
    print(array)

if __name__ == '__main__':
    array = [2,1,8,7,6,5]
    next_greater_number(array)
    array = [1,2,3,4]
    next_greater_number(array)
    array = [4,3,2,1]
    next_greater_number(array)
    array = [5,3,4,9,7,6]
    next_greater_number(array)
    array = [5,3,4,9,7,1]
    next_greater_number(array)
