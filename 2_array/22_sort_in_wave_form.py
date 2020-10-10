def wave_sort_simple(array):
    array.sort()
    for i in range(0,len(array)-1,2):
        array[i],array[i+1] = array[i+1],array[i]
    print(array)

def wave_sort(array):
    for i in range(0,len(array),2):
        if i>0 and array[i-1] > array[i]:
            array[i-1],array[i] = array[i],array[i-1]
        if i<len(array)-1 and array[i+1]>array[i]:
            array[i+1],array[i]=array[i],array[i+1]
    print(array)


if __name__ == "__main__":
    array = [1,2,3,4,5,6,7]
    wave_sort_simple(array)
    array = [1,2,3,4,5,6,7]
    wave_sort(array)
    arr = [10, 90, 49, 2, 1, 5, 23]
    wave_sort_simple(arr)
    arr = [10, 90, 49, 2, 1, 5, 23]
    wave_sort(arr)