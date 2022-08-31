def fibbonacci(val):
    sum= 0
    a = 1  
    b = 1
    while b < val:
        if b%2 == 0:
            sum += b
        h = a + b
        a = b
        b = h
    return sum  
print(fibbonacci(4000000))
