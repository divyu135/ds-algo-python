def number_of_triangles_naive(array):
    n = len(array)
    count=0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                 if array[i] < array[j] + array[k] and array[j] < array[i] + array[k] and array[k] < array[j] + array[i] :
                        count+=1
    print(count)

def number_of_triangles_improved(array):
    array.sort()
    n = len(array)
    count=0
    for i in range(0,n-2):
        k = i + 2
        for j in range(i+1,n-1):
            while k < n and array[i]+array[j]>array[k]:
                k+=1
            count+= (k-j-1)
    print(count)

if __name__ == "__main__":
    array = [4, 6, 3, 7]
    number_of_triangles_naive(array)
    number_of_triangles_improved(array)
    array = [10, 21, 22, 100, 101, 200, 300]
    number_of_triangles_naive(array)
    number_of_triangles_improved(array)

