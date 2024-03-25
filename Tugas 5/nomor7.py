# Output = 1 1 2 3 5 8 13 21 34 55

a, b = 1, 1
length = 8

print(a, b, end=' ')
for i in range(length):
    c = a + b 
    print(c, end=' ')
    a = b
    b = c
print()