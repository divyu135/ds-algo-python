def subarray_equal_0_1_simple(array):
    l = len(array)
    max_len,low,high  = 0,0,0
    for i in range(l):
        for j in range(i,l):
            c0,c1 = 0,0
            for k in range(i,j+1): 
                if array[k]==0:
                    c0+=1
                else:
                    c1+=1
            if c1==c0 and (j-i) > max_len:
                low = i
                high = j
                max_len = j-i
    print(low,high)

def subarray_equal_0_1_hash(array):
    lowest_index={}
    l,u,s=None,None,0
    _sum = 0

    for i,ele in enumerate(array):
        if ele == 0:
            _sum-=1
        else:
            _sum+=1
    
        if _sum == 0:
            u = i
            s = i+1
            l = i-s+1
            
        if lowest_index.get(_sum) == None:
            lowest_index[_sum]=i
        else:
            if i-lowest_index.get(_sum) > s:
                l = lowest_index.get(_sum)+1
                u = i
                s = i-lowest_index.get(_sum)
                # print("lus",l,u,s,_sum)
                # print()
    
    print(l,u)

if __name__ == '__main__':
    array = [1, 0, 0, 1, 0, 1, 1]
    subarray_equal_0_1_simple(array)
    subarray_equal_0_1_hash(array)
    print()
    array = [0, 0, 1, 1, 0]
    subarray_equal_0_1_simple(array)
    subarray_equal_0_1_hash(array)
    print()
    array = [1,0,1,1,0,1,0,1, 0, 1, 1, 1, 0, 0,1,1,0,0]
    subarray_equal_0_1_simple(array)
    subarray_equal_0_1_hash(array)