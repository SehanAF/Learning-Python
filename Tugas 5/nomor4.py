# Output =    7 x 6 = 42
            # 7 x 7 = 49
            # 7 x 8 = 56
            # 7 x 9 = 63
            # 7 x 10 = 70
            
a = 7
b = 5

for hitung in range (5):
    a = a
    b += 1
    hasil = a * b
    
    print(f"{a} x {b} = {hasil}")
    
print()