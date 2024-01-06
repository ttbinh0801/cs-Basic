# Câu 6: Tính tổng các số lẻ từ 1 đến n (với n là số nguyên dương được nhập từ bàn phím)
n=  int(input('nhập n:'))
u=0
for i in range(1,n+1,2):
    u += i 
print (u)


