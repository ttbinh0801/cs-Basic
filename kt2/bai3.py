# Câu 3: Cho danh sách numbers = [1, 4, "e", 2, 6, 8, "a", "b"].
    # a. Tính tổng các số trong danh sách numbers
    # b. Tính tích các số trong danh sách numbers
    # c. Tìm giá trị lớn nhất trong danh sách numbers
    # d. Tìm giá trị nhỏ nhất trong danh sách numbers

list_item = [1, 4, "e", 2, 6, 8, "a", "b"]
list_numbers=[]
for i in (list_item) :
        if  isinstance (i, int):
            list_numbers.append(i)
if 0 in list_numbers :
    print (0)  
else:
    u=1
    for k in list_numbers:
        u *= k
    print(u)
a= sum(list_numbers)
print(a)
list_numbers.sort(reverse=True)
print(list_numbers[0:1])
print(list_numbers[4:5])
 



            

    
