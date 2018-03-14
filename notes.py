def mystery(lst):
    for sublist in lst:
        total = 0
        for num in sublist:
            total = total + num
 
    return total


print(mystery([[10, 20], [20], [40, 10]]))
