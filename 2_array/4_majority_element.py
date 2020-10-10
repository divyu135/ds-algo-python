def majority_element_linearsearch(array):
    i=0
    count=1
    while i<len(array)-1:
        if array[i] == array[i+1]:
            count+=1
            if count > len(array)/2:
                return array[i]
        else:
            count=1
        i+=1
    return None

def frequency(array, item):
    count=0
    for ele in array:
        if ele == item:
            count+=1
    return count  

def majority_element_linearsearch_improved(array):
    mid = len(array)//2
    possible = array[mid]
    count = frequency(array,possible)
    if count > mid:
        return possible
    return None

def majority_element_mooreys_voting(array):
    major = array[0]
    vote = 0
    for ele in array:
        if ele == major:
            vote+=1
        else:
            vote-=1
        if vote == 0:
            major = ele
            vote = 1
            
    if vote > 0:
        if frequency(array, major) > len(array)/2:
            return major
        return None
    else:
        return None

if __name__ == '__main__' :
    array = [1,2,2,3,3,3,3,3,3,5]
    print("Majority Element: ", majority_element_linearsearch(array) )
    print("Majority Element: ", majority_element_linearsearch_improved(array) )
    print("Majority Element: ", majority_element_mooreys_voting(array))
    print()
    array = [1,2,2,3,3]
    print("Majority Element: ", majority_element_linearsearch(array) )
    print("Majority Element: ", majority_element_linearsearch_improved(array) )
    print("Majority Element: ", majority_element_mooreys_voting(array))
    print()
    array = [7,2,7,3,7,2,7,7]
    print("Majority Element: ", majority_element_linearsearch(sorted(array)) )
    print("Majority Element: ", majority_element_linearsearch_improved(sorted(array)) )
    print("Majority Element: ", majority_element_mooreys_voting(array))