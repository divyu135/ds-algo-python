def swap_bits(x,i,j):
    if ( (x>>i)&1 != (x>>j)&1 ):
        mask = (1<<i) | (1<<j)
        x = x ^ mask
    return x

x = 0b01001001
i = 0
j = 3
print(bin(swap_bits(x,i,j)))

x = 0b01001001
i = 1
j = 6
print(bin(swap_bits(x,i,j)))

x = 0b01001001
i = 1
j = 4
print(bin(swap_bits(x,i,j)))