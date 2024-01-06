numbers = [2, 7, 11, 5]
target = int(input('nhập số:'))
for i in range (len(numbers)):
    for j in range (i+1,len(numbers)) :
        if numbers[i]+numbers[j]== target:
            print([i,j]) 
        else:
            print('không có số thoả mãn')

