lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lis)



lis = [2, 4, 6, 8]
lis1 = [1, 3, 5, 7]
lis.extend(lis1)
print(lis)



lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in lis:
    if i % 2 ==0:
        print(i, "Even")
    else:
        print(i, "Odd")
