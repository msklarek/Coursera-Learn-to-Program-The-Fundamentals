
def averages(grades):
    
    '''(list) -> list

    Retrun a new list in which each item is the average
    of the grades in the inner list at the corresponding position of grades.
    >>>averages([[70,75,80],[70,80,90,100],[80,100]]
    [75.0, 85.0, 90.0]
    '''
    
    new_list = []

    for i in grades:
        
        total = 0
        for j in i:
            total = total + j
        new_list.append(total / len(i))
    print(new_list)
