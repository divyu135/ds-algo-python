def trapping_rainwater_approach1(array):
    water = 0
    for i in range(len(array)):
        left = max(array[:i+1])
        right = max(array[i:len(array)])
        min_both  = min(left,right)
        water += min_both - array[i]
        
    print(water)

def trapping_rainwater_approach2(array):
    water = 0
    left = [array[0]]
    right = [array[-1]]

    for i in range(1,len(array)):
        if array[i]>left[i-1]:
            left+=[array[i]]
        else:
            left+=[left[i-1]]
        if array[-i-1]>right[i-1]:
            right+=[array[-i-1]]
        else:
            right+=[right[i-1]]
    
    for i in range(len(array)):
        water += min(left[i],right[-i-1]) - array[i]

    print(water)

def trapping_rainwater_approach3(array):
    l = 0
    r = len(array)-1
    right_max = 0
    left_max = 0
    water = 0
    while l<r:
        if array[l] < array[r]:
            if array[l] > left_max:
                left_max=array[l]
            else:
                water += left_max - array[l]
            l+=1
        else:
            if array[r] > right_max:
                right_max=array[r]
            else:
                water += right_max-array[r]
            r-=1
    print(water)
if __name__ == "__main__":
    arr = [3,0,0,2,0,4]
    trapping_rainwater_approach1(arr)
    trapping_rainwater_approach2(arr)
    trapping_rainwater_approach3(arr)
    print()
    arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    trapping_rainwater_approach1(arr)
    trapping_rainwater_approach2(arr)
    trapping_rainwater_approach3(arr)

