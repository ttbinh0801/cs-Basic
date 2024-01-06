menu ={}
while True :
    print('1.thêm món ăn')
    print('2.xem menu')
    print('3.chỉnh sửa thông tin 1 món ăn ')
    print('4.xoá 1 món ăn')
    choice= int(input('lựa chon:'))
    if choice== 2:
        print(menu)
    elif choice==1:
        menu[input('món ăn muốn thêm:')]= input(':')
        print('thêm thành công')
    elif choice ==3:
        a = input('món ăn muốn sửa:')
        b =input('được sửa thành')
        menu[a]= b 
        print('sửa thành công')
    elif choice ==4:
        c= input('món muốn xoá')
        del menu[c]

