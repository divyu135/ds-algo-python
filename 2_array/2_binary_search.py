def binary_search( array, num ) :
    array = sorted(array)
    left = 0
    right = len(array)
    while left<right:
        mid = (left+right)//2
        if num == array[mid]:
            return True
        elif num > array[mid]:
            left = mid+1
        else :
            right = mid-1

if __name__ == "__main__":
    array = [1,2,5,7,1,3,56,8,2,7,0,6,2,21,567,8]
    num = 8
    if binary_search(array, num):
        print(num, " is present in the array")
    else:
        print(num, " is not present in the array")
