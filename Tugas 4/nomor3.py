# Tuliskan program untuk menentukan bilangan itu bilangan positif, negatif atau 0

a = 15
b = 15
c = 40

if a > b and a > c:
    print(f"bilangan {a} lebih besar dibanding {b} dan {c}")
elif b > a and a > c:
    print(f"bilangan {b} lebih besar dibanding {a} dan {c}")
elif c > a and c > b:
    print(f"bilangan {c} lebih besar dibanding {a} dan {b}")
    
elif a == b and a > c:
    print(f"bilangan {a} sama dengan {b}, tapi lebih besar dari {c}")
elif b == c and b > a:
    print(f"bilangan {b} sama dengan {c}, tapi lebih besar dari {a}")
elif c == a and c > b:
    print(f"bilangan {c} sama dengan {a}, tapi lebih besar dari {b}")
else:
    print(f"Semua angka adalah sama besar.")

