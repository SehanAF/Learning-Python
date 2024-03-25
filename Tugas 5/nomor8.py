

a, b, c = 1, 2, 3
length = 7

print(a, b, c, end=' ')
for i in range(length):
    d = a + b + c 
    print(d, end =' ')
    
    a = b
    b = c
    c = d
print()