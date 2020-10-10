def smallest_sum_not_possible(arr):
    arr.sort()
    smallest_s = 1
    i=0
    while i < len(arr) and arr[i]<=smallest_s:
        smallest_s+=arr[i]
        i+=1
    print(smallest_s)

if __name__ == '__main__':
    arr = [1, 3, 6, 10, 11, 15]
    smallest_sum_not_possible(arr)
    arr = [1, 1, 1, 1]
    smallest_sum_not_possible(arr)
    arr = [1, 1, 3, 4]
    smallest_sum_not_possible(arr)
    arr = [1, 2, 5, 10, 20, 40]
    smallest_sum_not_possible(arr)
    arr = [1, 2, 3, 4, 5, 6]
    smallest_sum_not_possible(arr)
