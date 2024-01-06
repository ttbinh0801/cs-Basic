def hamso(so):
    for i in range(len(so)):
        for j in range (1,len(so)-i-1):
            if so[j] >so [j+1]:
                temp = so[j]
                so[j]= so[j+1]
                so[j+1]= temp
    print(so)
hamso([1, 3, 5, 3, 7, 5, 9])

