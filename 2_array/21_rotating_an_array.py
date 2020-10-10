def left_rotating_array_approach1(array,d):
    temp = []
    n = len(array)
    i,j,k=0,0,0

    while k < d:
        temp+= [array[i]]
        k+=1
        i+=1
    while k < n:
        array[j] = array[k]
        k+=1
        j+=1
    i=0
    while j<n:
        array[j] = temp[i]
        j+=1
        i+=1

    print(array)

def left_rotating_array_approach2(array,d):
    n = len(array)
    for i in range(d):
        temp = array[0]
        for j in range(1,n):
            array[j-1] = array[j]
        array[n-1]=temp
    print(array)


def left_rotating_array_approach3(array,d):
    
    def gcd(a,b):
        if b==0:
            return a
        return gcd(b,a%b)

    n = len(array)
    gcd = gcd(n,d)

    for i in range(gcd):
        temp = array[i]
        j = i 
        while True:
            k = j + d
            if k>=n:
                k = k - n
            if k == i :
                break
            array[j] = array[k]
            j = k
        array[j] = temp
        
    print(array)

def left_rotating_array_approach4(array, d):
    n=len(array)
    for i in range(d//2):
        array[i],array[d-i-1] = array[d-i-1],array[i]
    for j in range(n//2):
        array[j+d],array[-j-1] = array[-j-1],array[j+d]
    for k in range(n//2):
        array[k],array[-k-1] = array[-k-1],array[k]
    print(array)
if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    left_rotating_array_approach1(array,3)
    array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    left_rotating_array_approach2(array,3)
    array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    left_rotating_array_approach3(array,3)
    array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    left_rotating_array_approach4(array,3)
