# Câu 5: Viết một chương trình Python để kiểm tra xem một số nguyên đã cho có chia hết cho cả 3 và 5 không?
x= int(input('nhập x:'))
if x % 5 == 0 :
    if x % 3 == 0 :
        print ('x là số chia hết cho cả 3 và 5')
    else :
        print ('không phải')
else: 
    print('không phải')        
