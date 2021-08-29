# Do following in O(1)
    
# 1. Right propogate the rightmost set bit.
test = [0b1010000, 0b100000, 0b101, 0b010]
for x in test:
    x = x | (x-1)
    print(bin(x))

# 2. Compute X mod power of 2 
x,y = 77, 64
mod = x & (y-1) 
print("x={} {} y={} {} mod={} {}".format(x,bin(x),y, bin(y),mod, bin(mod)))

    
# 3. Test if x is power of 2 
test = [0,1,2,4,8,32,64,128,5,9,10,20,31]
# x & (x-1) will be 0
for x in test:
    print("x={} is power of 2: {}".format(x, x & (x-1) is 0))
