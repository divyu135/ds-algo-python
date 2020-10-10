def linear_search(array, num):
    for ele in array:
        if ele == num:
            return True
    return False

if __name__ == "__main__":
    array = [1,2,5,7,1,3,56,8,2,7,9,6,2,21,567,8]
    num = 9
    if linear_search(array, num):
        print(num, " is present in the array")
    else:
        print(num, " is not present in the array")