def find_pairs_naive( array, _sum ):
    for i in range( len( array ) ):
        target = _sum - array[i]
        for ele in array[i+1:]:
            if ele == target:
                print(array[i],ele)

def find_pairs_hashtable( array, _sum):
    hashtable = {}
    for ele in array:
        target = _sum - ele
        if hashtable.get(target):
            print(ele,target)
        else:
            hashtable[ele]=1 

if __name__ == '__main__':
    array = [4,8,2,9,1,6,5,0]
    _sum = 6
    find_pairs_naive(array,_sum)
    print()
    find_pairs_hashtable(array,_sum)
