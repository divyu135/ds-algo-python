def find_product_array(array):
    products = []
    temp=1
    for i in range(len(array)):
        products+= [temp] 
        temp*=array[i]
    temp=1
    for i in range(len(products)):
        products[-i-1]*=temp
        temp*=array[-i-1]

    return products

if __name__ == "__main__":
    array = [10, 3, 5, 6, 2]
    print(find_product_array(array))
    print()
    array = [1, 2, 3, 4, 5]
    print(find_product_array(array))
    print()
    array = [2, 3, 4, 10]
    print(find_product_array(array))
    print()