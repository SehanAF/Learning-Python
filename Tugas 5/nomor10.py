# Output =  2 3 2 3 2
#           3 2 3 2
#           2 3 2
#           3 2
#           2

length = 5 
for i in range(length):
    for j in range(length):
        if i % 2 == 0:
            if j % 2 == 0:
                print("2", end=' ')
            else:
                print("3", end=' ')
        else:
            if j % 2 == 1:
                print("2", end=' ')
            else:
                print("3", end=' ')
    print()
    length -= 1