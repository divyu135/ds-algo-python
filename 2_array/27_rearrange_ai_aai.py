def rearrange_extra_space(array):
    temp=[]
    for i in range(len(array)):
        temp+=[array[array[i]]]
    print(temp)

def rearrange(array):
    n=len(array)
    for i in range(n):
        array[i] = array[i]+(array[array[i]]%n)*n
    for i in range(n):
        array[i] //= n
    print(array)
    
if __name__ == "__main__":
    array = [ 3,1,0,2,4]
    rearrange_extra_space(array)
    rearrange(array)