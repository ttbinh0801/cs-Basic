# Câu 8: Cho một số nguyên n, hãy tính tổng các số chẳn từ 1 đến n sử dụng vòng lặp while.
n=  int(input('nhập n:'))
# u=0
# while u<=n :
#     if u %2 == 0 :
#         u += u
# print (u)


# n = int(input())
total = 0
current_number = 1
while current_number <= n:
    if current_number % 2 == 0:
        total+=current_number
    current_number+=1
print(total)


    


        
