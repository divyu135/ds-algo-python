#Bruteforce approach to find the parity of a word
def parity(x):
    result = 0 
    while x:
        result ^= x & 1
        x >>= 1
    return result

num = 64
print("Number: {} Binary: {} Parity {}".format(num, bin(num), parity(num)) )
