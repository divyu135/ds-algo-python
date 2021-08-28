# Improve bruteforce by erasing the lowest set bit

def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= (x-1)
    return result

num = 64
print("Number: {} Binary: {} Parity {}".format(num, bin(num), parity(num)) )
num = 23
print("Number: {} Binary: {} Parity {}".format(num, bin(num), parity(num)) )
num = 21
print("Number: {} Binary: {} Parity {}".format(num, bin(num), parity(num)) )
