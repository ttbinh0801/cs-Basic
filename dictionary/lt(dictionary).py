# khởi tạo dict với cặp key-value
# CRUD: Create - C
        # read - R
        # update - U
        # delete - D
# C

# print(register["email"])

# R
# email=input('email')
# password=input('pass')
# if (email == register['email']) and (password == register['password']):
#     print('đăng nhập thành công')
# else:
#     print('k thành công')

# U
# register['email']='b@gmail.com'
# add new key-vaue 
# register['confirm_email']='b@gmail.com'
# print(register)

# D
# del register['email']

register= {
    "first name":"bình",
    "last name":"trần thanh",
    'email': "binh@gmail.com",
    "password":"123"
}


register_account={}

while True :
    print('1.sign up')
    print('2.sign in')
    choice= int(input('lựa chon:'))
    if choice==1 :
        firstname = input('tên :')
        lastname = input('tên đệm')
        email = input('email:')
        password = input('pass:')
        register_account['firstname']= firstname
        register_account['lastname']= lastname
        register_account['email']= email
        register_account['password']= password
        print('đky thành công')
    elif choice==2 :
        email = input('email:')
        password = input('pass:')
        while (email != register_account['email']) :
            email = input('nhập lại mật khẩu: ')
        if (email == register_account['email']) :
            print('đăng nhập thành công')
    else :
        break 
# tạo điều kiện cho email (nếu nhập k đúng -> in: nhập lại)








