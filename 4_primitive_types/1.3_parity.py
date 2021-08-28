# We can reduce the timecomplexity using lookup table
# bitmasksize = 16
# BitMask = 0xFFFF
# PrecomputedParity[x>>(3*bitmasksize)] ^ PrecomputedParity[x>>(2*bitmasksize) & BitMask] ^ 
# PrecomputedParity[x>>(1*bitmasksize) & BitMask] ^ PrecomputedParity[x & BitMask] 

# Furhter reduce the time complexity by using XOR property
def parity(x):
    x ^= x>>32
    x ^= x>>16
    x ^= x>>8
    x ^= x>>4
    x ^= x>>2
    x ^= x>>1
    return x & 0x1

num = 64
print("Number: {} Binary: {} Parity {}".format(num, bin(num), parity(num)) )
num = 23
print("Number: {} Binary: {} Parity {}".format(num, bin(num), parity(num)) )
num = 21
print("Number: {} Binary: {} Parity {}".format(num, bin(num), parity(num)) )