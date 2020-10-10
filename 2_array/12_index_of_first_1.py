# Given a list of o and 1 with unknown size, all zeroes appearing first and then 1
# Fins the starting index of 1

def index_of_first_1_binarysearch(array):
    l=0
    r=len(array)-1
    if array[0]==1:
        return 0
    while l<=r:
        mid = (l+r)//2
        if array[mid]==1 and array[mid-1]==0:
            return mid
        elif array[mid]==0:
            l = mid+1
        else:
            r = mid-1
    return None
        
if __name__ == '__main__':
    array = [0,0,0,1]
    print(index_of_first_1_binarysearch(array))